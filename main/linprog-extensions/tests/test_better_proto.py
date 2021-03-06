
from dataclasses import dataclass
from os import name
from google.protobuf.json_format import ParseDict, MessageToDict

from context import operations_research
from operations_research.linear_extension_pb2 import(
    ReferenceMPModel as ReferenceMPModel_pb2,
    ExtendedMPModel as ExtendedMPModel_pb2,
)
from operations_research.linear_solver_pb2 import(
    MPVariableProto as MPVariableProto_pb2,
    MPModelProto as MPModelProto_pb2,
)

from server.linprog_structs.operations_research import(
    ReferenceMPModel,
    MPVariableProto,
    ReferenceMPModelRequest,
    ExtendedMPModel,
)
from server.linprog_structs.operation_research_ext import(
    ExtendedMPModelExt,
    MPModelProtoExt,
    ReferenceMPModelExt,
)


def test_bp_sp_obj_creation():
    betterproto_obj = ReferenceMPModel()
    betterproto_obj.name = "bp_test_model_one"
    betterproto_obj.variables.append(
        MPVariableProto(name="bp_test_var_one")
    )

    standardproto_obj = ReferenceMPModel_pb2()
    standardproto_obj.name = "sp_test_model_one"
    standardproto_obj.variables.extend([
        MPVariableProto_pb2(name="sp_test_var_one")
    ])

    ## okay so we created these two versions of the same structure
    ## now what? Question is how they relate or can interact
    return


def test_append_standard_proto_to_betterproto():

    betterproto_obj = ReferenceMPModel()
    betterproto_obj.name = "bp_test_model_one"
    betterproto_obj.variables.append(
        MPVariableProto(name="bp_test_var_one")
    )

    standardproto_variable =  MPVariableProto_pb2(name="sp_test_var_two")
    betterproto_obj.variables.append(standardproto_variable)
    ## okay so bp does not throw any errors if you put this SP in there (as a List)
    ## I think for that matter it won't even complain if you put anything
    ## I think it should be a similar behaviour even for the other way (i.e put a bp in sp as list)
    ## the main thing that is not tested here is the case for non-list objects.

    return


def test_put_sp_into_bp():

    sp_conc_model = MPModelProto_pb2()
    sp_conc_model.name = "sp_test_model_one"
    sp_extended_model = ExtendedMPModel_pb2()
    sp_extended_model.concrete_model.CopyFrom(sp_conc_model)

    bp_model_request = ReferenceMPModelRequest(model = sp_extended_model)

    ## okay so here also seems that bp is pretty permissive in accepting objects of non-mathcing type.
    ## general practice of python like python!
    ## but I guess it will not properly convert them to binaries and back
    ## also what about the other way? I don't think we can add a bp to sp
    return 


def test_normal_betterproto_creation():

    bp_ref_model = ReferenceMPModel()
    bp_ref_model.name = "test_model"
    bp_ref_model.variables.append(
        MPVariableProto(name="test_var1")
    )
    bp_extended_model = ExtendedMPModel()
    bp_extended_model.reference_model = bp_ref_model
    obj_to_dict = bp_extended_model.to_dict()
    assert( isinstance(obj_to_dict, dict) )

    # test serialize
    serialized = bytes(bp_extended_model)
    bp_extended_model_from_binary  = ExtendedMPModelExt().parse(serialized)
    obj_to_dict2 = bp_extended_model_from_binary.to_dict()

    # okay so here we normally create a bp obj, i.e not from sp message, we populate, serialize, and then back
    # works as expected
    return


def test_normal_betterproto_creation_alternative():

    bp_ref_model = MPModelProtoExt(
        name="test_model",
        variable = [MPVariableProto(name="test_var1"), MPVariableProto(name="test_var2")]
    )
    bp_extended_model = ExtendedMPModelExt(
        concrete_model=bp_ref_model
    )
    obj_to_dict = bp_extended_model.to_dict()
    assert( isinstance(obj_to_dict, dict) )

    # test serialize

    serialized = bytes(bp_extended_model)
    bp_extended_model_unserialized  = ExtendedMPModelExt().parse(serialized)
    obj_to_dict2 = bp_extended_model_unserialized.to_dict()

    data4 = ExtendedMPModelExt().from_dict(obj_to_dict2)
    obj_to_dict3 = data4.to_dict()

    # here we create the bp obj a bit different, i.e not creating an empty object, then populate,
    # still works fine as expected.
    return


def test_standard_proto_to_better_proto():

    sp_conc_model =MPModelProto_pb2()
    sp_conc_model.name = "test_model3"
    sp_conc_model.variable.append(
        MPVariableProto_pb2(
            name = "test_variable_1"
        )
    )
    sp_extended_model = ExtendedMPModel_pb2()
    sp_extended_model.concrete_model.CopyFrom(sp_conc_model)


    bp_extended_model = ExtendedMPModelExt.from_proto(sp_extended_model)
    obj_to_dict = bp_extended_model.to_dict()
    assert( isinstance(obj_to_dict, dict) )
    # okay this is okay

    bp_ref_model = MPModelProtoExt(
        name="test_model_x",
    )

    bp_extended_model_two = ExtendedMPModelExt(
        concrete_model=bp_ref_model,
        reference_model=ReferenceMPModelExt(),
    )

    # test serialize
    serialized = bytes(bp_extended_model)
    bp_extended_model_unserialized  = ExtendedMPModelExt().parse(serialized)
    obj_to_dict2 = bp_extended_model_unserialized.to_dict()
    assert(obj_to_dict2 == obj_to_dict)

    # serialized

    serialized_two = bytes(bp_extended_model_two)
    bp_extended_model_unserialized_two  = ExtendedMPModelExt().parse(serialized_two)
    obj_to_dict3 = bp_extended_model_unserialized_two.to_dict()

    return


def test_proto_to_dict_to_proto():

    sp_conc_model = MPModelProto_pb2()
    sp_conc_model.name = "test_model3"
    sp_conc_model.variable.append(
        MPVariableProto_pb2(
            name = "test_variable_1"
        )
    )
    sp_extended_model = ExtendedMPModel_pb2()
    sp_extended_model.concrete_model.CopyFrom(sp_conc_model)
    obj_to_dict1 = MessageToDict(sp_extended_model)
    
    bp_extended_model = ExtendedMPModelExt()
    bp_extended_model.from_dict(obj_to_dict1)

    obj_to_dict2 = bp_extended_model.to_dict()
    return



if __name__ == "__main__":

    # test_bp_sp_obj_creation()
    # test_append_standard_proto_to_betterproto()
    # test_put_sp_into_bp()
    # test_normal_betterproto_creation()
    test_normal_betterproto_creation_alternative()
    test_standard_proto_to_better_proto()

    # test_proto_to_dict_to_proto()