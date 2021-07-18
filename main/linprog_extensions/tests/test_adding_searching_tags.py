from dataclasses import dataclass
from os import name
from google.protobuf.json_format import ParseDict, MessageToDict

from context import operations_research


from server.linprog_structs.operation_research_ext import(
    ExtendedMPModelExt,
    MPModelProtoExt,
    ReferenceMPModelExt,
    ReferenceMPModelRequestStreem,
)


from build_reference_model.basic_model_instantiation_from_proto import instantiate_model

def test_adding_tags():


    model_requests = instantiate_model()
    request_stream_struct = ReferenceMPModelRequestStreem.from_proto(model_requests)

    


    return





    







if __name__ == "__main__":
    
    test_adding_tags()