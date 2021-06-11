# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mip.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import linear_solver_pb2 as linear__solver__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mip.proto',
  package='operations_research',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tmip.proto\x12\x13operations_research\x1a\x13linear_solver.proto2h\n\nMIPService\x12Z\n\x08MIPModel\x12#.operations_research.MPModelRequest\x1a\'.operations_research.MPSolutionResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[linear__solver__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MIPSERVICE = _descriptor.ServiceDescriptor(
  name='MIPService',
  full_name='operations_research.MIPService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=55,
  serialized_end=159,
  methods=[
  _descriptor.MethodDescriptor(
    name='MIPModel',
    full_name='operations_research.MIPService.MIPModel',
    index=0,
    containing_service=None,
    input_type=linear__solver__pb2._MPMODELREQUEST,
    output_type=linear__solver__pb2._MPSOLUTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MIPSERVICE)

DESCRIPTOR.services_by_name['MIPService'] = _MIPSERVICE

# @@protoc_insertion_point(module_scope)
