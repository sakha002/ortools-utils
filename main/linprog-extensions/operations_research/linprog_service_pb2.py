# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operations_research/linprog_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from operations_research import linear_solver_pb2 as operations__research_dot_linear__solver__pb2
from operations_research import linear_extension_pb2 as operations__research_dot_linear__extension__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='operations_research/linprog_service.proto',
  package='operations_research',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)operations_research/linprog_service.proto\x12\x13operations_research\x1a\'operations_research/linear_solver.proto\x1a*operations_research/linear_extension.proto2\xcb\x02\n\x0eLinProgService\x12[\n\tMILPModel\x12#.operations_research.MPModelRequest\x1a\'.operations_research.MPSolutionResponse\"\x00\x12o\n\x12MILPReferenceModel\x12,.operations_research.ReferenceMPModelRequest\x1a\'.operations_research.MPSolutionResponse\"\x00(\x01\x12k\n\x12MILPReferenceBuild\x12,.operations_research.ReferenceMPModelRequest\x1a#.operations_research.MPModelRequest\"\x00(\x01\x62\x06proto3'
  ,
  dependencies=[operations__research_dot_linear__solver__pb2.DESCRIPTOR,operations__research_dot_linear__extension__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LINPROGSERVICE = _descriptor.ServiceDescriptor(
  name='LinProgService',
  full_name='operations_research.LinProgService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=152,
  serialized_end=483,
  methods=[
  _descriptor.MethodDescriptor(
    name='MILPModel',
    full_name='operations_research.LinProgService.MILPModel',
    index=0,
    containing_service=None,
    input_type=operations__research_dot_linear__solver__pb2._MPMODELREQUEST,
    output_type=operations__research_dot_linear__solver__pb2._MPSOLUTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MILPReferenceModel',
    full_name='operations_research.LinProgService.MILPReferenceModel',
    index=1,
    containing_service=None,
    input_type=operations__research_dot_linear__extension__pb2._REFERENCEMPMODELREQUEST,
    output_type=operations__research_dot_linear__solver__pb2._MPSOLUTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MILPReferenceBuild',
    full_name='operations_research.LinProgService.MILPReferenceBuild',
    index=2,
    containing_service=None,
    input_type=operations__research_dot_linear__extension__pb2._REFERENCEMPMODELREQUEST,
    output_type=operations__research_dot_linear__solver__pb2._MPMODELREQUEST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LINPROGSERVICE)

DESCRIPTOR.services_by_name['LinProgService'] = _LINPROGSERVICE

# @@protoc_insertion_point(module_scope)