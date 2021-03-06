# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video_popup.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='video_popup.proto',
  package='video_popup',
  syntax='proto2',
  serialized_pb=_b('\n\x11video_popup.proto\x12\x0bvideo_popup\"\xe3\x01\n\x10NeighborhoodPara\x12\x1d\n\x0fvelocity_weight\x18\x01 \x01(\x02:\x04\x32\x30\x30\x30\x12\x1a\n\x0etop_frames_num\x18\x02 \x01(\x05:\x02-1\x12\x1d\n\x0e\x64ist_threshold\x18\x03 \x01(\x02:\x05\x31\x30\x30\x30\x30\x12\x1e\n\x11occlusion_penalty\x18\x04 \x01(\x02:\x03\x35\x30\x30\x12 \n\x14max_occlusion_frames\x18\x05 \x01(\x05:\x02\x34\x35\x12\x19\n\x0c\x63olor_weight\x18\x06 \x01(\x02:\x03\x32.5\x12\x18\n\x0cneighbor_num\x18\x07 \x01(\x05:\x02\x31\x30\"X\n\x16GRICModelSelectionPara\x12\x13\n\x05noise\x18\x01 \x01(\x02:\x04\x30.05\x12\x12\n\x07lambda1\x18\x02 \x01(\x02:\x01\x31\x12\x15\n\x07lamnda2\x18\x03 \x01(\x02:\x04\x30.01\"\x89\x02\n\x10PerspFittingPara\x12\x42\n\nfh_fitting\x18\x01 \x01(\x0e\x32\'.video_popup.PerspFittingPara.FHFitting:\x05\x46ONLY\x12J\n\rfitting_error\x18\x02 \x01(\x0e\x32*.video_popup.PerspFittingPara.FittingError:\x07\x41LGEBRA\",\n\tFHFitting\x12\t\n\x05\x46ONLY\x10\x00\x12\t\n\x05HONLY\x10\x01\x12\t\n\x05\x46\x41NDH\x10\x02\"7\n\x0c\x46ittingError\x12\x0b\n\x07\x41LGEBRA\x10\x00\x12\x0b\n\x07SAMPSON\x10\x01\x12\r\n\tGEOMETRIC\x10\x02\"\x12\n\x10OrthoFittingPara\"\x15\n\x13SubspaceFittingPara\"\xb7\x08\n\x10ModelFittingPara\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x11init_proposal_num\x18\x02 \x01(\x05:\x03\x32\x30\x30\x12\x11\n\x03mdl\x18\x03 \x01(\x02:\x04\x34\x30\x30\x30\x12\x14\n\titers_num\x18\x04 \x01(\x02:\x01\x35\x12\x39\n\x12persp_fitting_para\x18\x65 \x01(\x0b\x32\x1d.video_popup.PerspFittingPara\x12\x39\n\x12ortho_fitting_para\x18\x66 \x01(\x0b\x32\x1d.video_popup.OrthoFittingPara\x12?\n\x15subspace_fitting_para\x18g \x01(\x0b\x32 .video_popup.SubspaceFittingPara\x12H\n\rfitting_model\x18h \x01(\x0e\x32*.video_popup.ModelFittingPara.FittingModel:\x05PERSP\x12(\n\x18use_gric_model_selection\x18\xc9\x01 \x01(\x08:\x05\x66\x61lse\x12G\n\x19gric_model_selection_para\x18\xca\x01 \x01(\x0b\x32#.video_popup.GRICModelSelectionPara\x12\x43\n\x0egraph_cut_para\x18\xad\x02 \x01(\x0b\x32*.video_popup.ModelFittingPara.GraphCutPara\x1a\xde\x03\n\x0cGraphCutPara\x12H\n\x06\x65ngine\x18\x01 \x01(\x0e\x32\x31.video_popup.ModelFittingPara.GraphCutPara.Engine:\x05\x41LLGC\x12\x17\n\x0coverlap_cost\x18\x02 \x01(\x02:\x01\x31\x12$\n\x19pointwise_breaking_lambda\x18\x03 \x01(\x02:\x01\x31\x12#\n\x18pointwise_outlier_lambda\x18\x04 \x01(\x02:\x01\x31\x12!\n\x14pairwise_breaking_ma\x18\x05 \x01(\x02:\x03\x31\x30\x30\x12!\n\x14pairwise_breaking_mb\x18\x06 \x01(\x02:\x03\x31\x30\x30\x12 \n\x14pairwise_breaking_mc\x18\x07 \x01(\x02:\x02\x33\x30\x12\x1c\n\x0fpairwise_weight\x18\x08 \x01(\x02:\x03\x31\x30\x30\x12\x1a\n\x0epairwise_sigma\x18\t \x01(\x02:\x02\x31\x30\x12\x18\n\rneighbors_num\x18\n \x01(\x05:\x01\x35\x12\x1f\n\x14overlap_neighbor_num\x18\x0b \x01(\x05:\x01\x35\x12\x18\n\rlambda_weight\x18\x0c \x01(\x02:\x01\x31\")\n\x06\x45ngine\x12\t\n\x05\x41LPHA\x10\x00\x12\t\n\x05MULTI\x10\x01\x12\t\n\x05\x41LLGC\x10\x02\"2\n\x0c\x46ittingModel\x12\t\n\x05PERSP\x10\x00\x12\t\n\x05ORTHO\x10\x01\x12\x0c\n\x08SUBSPACE\x10\x02\"\x92\x01\n\x10SegmentationPara\x12\x13\n\x0btracks_path\x18\x01 \x01(\t\x12\x13\n\x0bimages_path\x18\x02 \x01(\t\x12\x19\n\x0emin_vis_frames\x18\x03 \x01(\x05:\x01\x35\x12\x39\n\x12model_fitting_para\x18\x65 \x01(\x0b\x32\x1d.video_popup.ModelFittingPara\"\xab\x01\n\x17OrthoReconstructionPara\x12\x12\n\x03MC1\x18\x01 \x01(\x02:\x05\x30.001\x12\x0f\n\x03MC2\x18\x02 \x01(\x02:\x02\x32\x30\x12\x0f\n\x03MC3\x18\x03 \x01(\x02:\x02\x31\x30\x12\x13\n\x08\x62\x61_model\x18\x04 \x01(\x05:\x01\x30\x12\x15\n\x07\x61lpha_s\x18\x05 \x01(\x02:\x04\x30.01\x12\x15\n\x07\x61lpha_z\x18\x06 \x01(\x02:\x04\x30.01\x12\x17\n\x0b\x61lpha_prior\x18\x07 \x01(\x02:\x02\x31\x30\"]\n\x17PerspReconstructionPara\x12\x0f\n\x02\x66x\x18\x01 \x01(\x02:\x03\x38\x30\x30\x12\x0f\n\x02\x66y\x18\x02 \x01(\x02:\x03\x38\x30\x30\x12\x0f\n\x02u0\x18\x03 \x01(\x02:\x03\x36\x34\x30\x12\x0f\n\x02v0\x18\x04 \x01(\x02:\x03\x33\x36\x30\"\xd2\x03\n\x12ReconstructionPara\x12\x61\n\x06method\x18\x01 \x01(\x0e\x32\x36.video_popup.ReconstructionPara.ReconstructionPipeline:\x19ORTHO_PIECEWISE_STITCHING\x12G\n\x19ortho_reconstruction_para\x18\x02 \x01(\x0b\x32$.video_popup.OrthoReconstructionPara\x12G\n\x19persp_reconstruction_para\x18\x03 \x01(\x0b\x32$.video_popup.PerspReconstructionPara\x12\x12\n\x06thresh\x18\x65 \x01(\x05:\x02\x35\x30\"\xb2\x01\n\x16ReconstructionPipeline\x12\x1d\n\x19ORTHO_PIECEWISE_STITCHING\x10\x00\x12\x1a\n\x16ORTHO_PIECEWISE_GLOBAL\x10\x01\x12\x10\n\x0cORTHO_GLOBAL\x10\x02\x12\x1d\n\x19PERSP_PIECEWISE_STITCHING\x10\x03\x12\x1a\n\x16PERSP_PIECEWISE_GLOBAL\x10\x04\x12\x10\n\x0cPERSP_GLOBAL\x10\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PERSPFITTINGPARA_FHFITTING = _descriptor.EnumDescriptor(
  name='FHFitting',
  full_name='video_popup.PerspFittingPara.FHFitting',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FONLY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HONLY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FANDH', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=519,
  serialized_end=563,
)
_sym_db.RegisterEnumDescriptor(_PERSPFITTINGPARA_FHFITTING)

_PERSPFITTINGPARA_FITTINGERROR = _descriptor.EnumDescriptor(
  name='FittingError',
  full_name='video_popup.PerspFittingPara.FittingError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALGEBRA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAMPSON', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEOMETRIC', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=565,
  serialized_end=620,
)
_sym_db.RegisterEnumDescriptor(_PERSPFITTINGPARA_FITTINGERROR)

_MODELFITTINGPARA_GRAPHCUTPARA_ENGINE = _descriptor.EnumDescriptor(
  name='Engine',
  full_name='video_popup.ModelFittingPara.GraphCutPara.Engine',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALPHA', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTI', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLGC', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1652,
  serialized_end=1693,
)
_sym_db.RegisterEnumDescriptor(_MODELFITTINGPARA_GRAPHCUTPARA_ENGINE)

_MODELFITTINGPARA_FITTINGMODEL = _descriptor.EnumDescriptor(
  name='FittingModel',
  full_name='video_popup.ModelFittingPara.FittingModel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PERSP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORTHO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBSPACE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1695,
  serialized_end=1745,
)
_sym_db.RegisterEnumDescriptor(_MODELFITTINGPARA_FITTINGMODEL)

_RECONSTRUCTIONPARA_RECONSTRUCTIONPIPELINE = _descriptor.EnumDescriptor(
  name='ReconstructionPipeline',
  full_name='video_popup.ReconstructionPara.ReconstructionPipeline',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORTHO_PIECEWISE_STITCHING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORTHO_PIECEWISE_GLOBAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORTHO_GLOBAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSP_PIECEWISE_STITCHING', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSP_PIECEWISE_GLOBAL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSP_GLOBAL', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2454,
  serialized_end=2632,
)
_sym_db.RegisterEnumDescriptor(_RECONSTRUCTIONPARA_RECONSTRUCTIONPIPELINE)


_NEIGHBORHOODPARA = _descriptor.Descriptor(
  name='NeighborhoodPara',
  full_name='video_popup.NeighborhoodPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='velocity_weight', full_name='video_popup.NeighborhoodPara.velocity_weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top_frames_num', full_name='video_popup.NeighborhoodPara.top_frames_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dist_threshold', full_name='video_popup.NeighborhoodPara.dist_threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=10000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='occlusion_penalty', full_name='video_popup.NeighborhoodPara.occlusion_penalty', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=500,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_occlusion_frames', full_name='video_popup.NeighborhoodPara.max_occlusion_frames', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=45,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color_weight', full_name='video_popup.NeighborhoodPara.color_weight', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=2.5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neighbor_num', full_name='video_popup.NeighborhoodPara.neighbor_num', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=262,
)


_GRICMODELSELECTIONPARA = _descriptor.Descriptor(
  name='GRICModelSelectionPara',
  full_name='video_popup.GRICModelSelectionPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='noise', full_name='video_popup.GRICModelSelectionPara.noise', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.05,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lambda1', full_name='video_popup.GRICModelSelectionPara.lambda1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lamnda2', full_name='video_popup.GRICModelSelectionPara.lamnda2', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.01,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=352,
)


_PERSPFITTINGPARA = _descriptor.Descriptor(
  name='PerspFittingPara',
  full_name='video_popup.PerspFittingPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fh_fitting', full_name='video_popup.PerspFittingPara.fh_fitting', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fitting_error', full_name='video_popup.PerspFittingPara.fitting_error', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERSPFITTINGPARA_FHFITTING,
    _PERSPFITTINGPARA_FITTINGERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=620,
)


_ORTHOFITTINGPARA = _descriptor.Descriptor(
  name='OrthoFittingPara',
  full_name='video_popup.OrthoFittingPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=640,
)


_SUBSPACEFITTINGPARA = _descriptor.Descriptor(
  name='SubspaceFittingPara',
  full_name='video_popup.SubspaceFittingPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=642,
  serialized_end=663,
)


_MODELFITTINGPARA_GRAPHCUTPARA = _descriptor.Descriptor(
  name='GraphCutPara',
  full_name='video_popup.ModelFittingPara.GraphCutPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='engine', full_name='video_popup.ModelFittingPara.GraphCutPara.engine', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_cost', full_name='video_popup.ModelFittingPara.GraphCutPara.overlap_cost', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pointwise_breaking_lambda', full_name='video_popup.ModelFittingPara.GraphCutPara.pointwise_breaking_lambda', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pointwise_outlier_lambda', full_name='video_popup.ModelFittingPara.GraphCutPara.pointwise_outlier_lambda', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairwise_breaking_ma', full_name='video_popup.ModelFittingPara.GraphCutPara.pairwise_breaking_ma', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairwise_breaking_mb', full_name='video_popup.ModelFittingPara.GraphCutPara.pairwise_breaking_mb', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairwise_breaking_mc', full_name='video_popup.ModelFittingPara.GraphCutPara.pairwise_breaking_mc', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=30,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairwise_weight', full_name='video_popup.ModelFittingPara.GraphCutPara.pairwise_weight', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairwise_sigma', full_name='video_popup.ModelFittingPara.GraphCutPara.pairwise_sigma', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='neighbors_num', full_name='video_popup.ModelFittingPara.GraphCutPara.neighbors_num', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_neighbor_num', full_name='video_popup.ModelFittingPara.GraphCutPara.overlap_neighbor_num', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lambda_weight', full_name='video_popup.ModelFittingPara.GraphCutPara.lambda_weight', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODELFITTINGPARA_GRAPHCUTPARA_ENGINE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1215,
  serialized_end=1693,
)

_MODELFITTINGPARA = _descriptor.Descriptor(
  name='ModelFittingPara',
  full_name='video_popup.ModelFittingPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='video_popup.ModelFittingPara.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_proposal_num', full_name='video_popup.ModelFittingPara.init_proposal_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=200,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mdl', full_name='video_popup.ModelFittingPara.mdl', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=4000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iters_num', full_name='video_popup.ModelFittingPara.iters_num', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='persp_fitting_para', full_name='video_popup.ModelFittingPara.persp_fitting_para', index=4,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ortho_fitting_para', full_name='video_popup.ModelFittingPara.ortho_fitting_para', index=5,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subspace_fitting_para', full_name='video_popup.ModelFittingPara.subspace_fitting_para', index=6,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fitting_model', full_name='video_popup.ModelFittingPara.fitting_model', index=7,
      number=104, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_gric_model_selection', full_name='video_popup.ModelFittingPara.use_gric_model_selection', index=8,
      number=201, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gric_model_selection_para', full_name='video_popup.ModelFittingPara.gric_model_selection_para', index=9,
      number=202, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph_cut_para', full_name='video_popup.ModelFittingPara.graph_cut_para', index=10,
      number=301, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MODELFITTINGPARA_GRAPHCUTPARA, ],
  enum_types=[
    _MODELFITTINGPARA_FITTINGMODEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=1745,
)


_SEGMENTATIONPARA = _descriptor.Descriptor(
  name='SegmentationPara',
  full_name='video_popup.SegmentationPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracks_path', full_name='video_popup.SegmentationPara.tracks_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='images_path', full_name='video_popup.SegmentationPara.images_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_vis_frames', full_name='video_popup.SegmentationPara.min_vis_frames', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_fitting_para', full_name='video_popup.SegmentationPara.model_fitting_para', index=3,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1748,
  serialized_end=1894,
)


_ORTHORECONSTRUCTIONPARA = _descriptor.Descriptor(
  name='OrthoReconstructionPara',
  full_name='video_popup.OrthoReconstructionPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MC1', full_name='video_popup.OrthoReconstructionPara.MC1', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.001,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MC2', full_name='video_popup.OrthoReconstructionPara.MC2', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MC3', full_name='video_popup.OrthoReconstructionPara.MC3', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ba_model', full_name='video_popup.OrthoReconstructionPara.ba_model', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alpha_s', full_name='video_popup.OrthoReconstructionPara.alpha_s', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.01,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alpha_z', full_name='video_popup.OrthoReconstructionPara.alpha_z', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.01,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alpha_prior', full_name='video_popup.OrthoReconstructionPara.alpha_prior', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1897,
  serialized_end=2068,
)


_PERSPRECONSTRUCTIONPARA = _descriptor.Descriptor(
  name='PerspReconstructionPara',
  full_name='video_popup.PerspReconstructionPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fx', full_name='video_popup.PerspReconstructionPara.fx', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=800,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fy', full_name='video_popup.PerspReconstructionPara.fy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=800,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='u0', full_name='video_popup.PerspReconstructionPara.u0', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=640,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v0', full_name='video_popup.PerspReconstructionPara.v0', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=360,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2070,
  serialized_end=2163,
)


_RECONSTRUCTIONPARA = _descriptor.Descriptor(
  name='ReconstructionPara',
  full_name='video_popup.ReconstructionPara',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='video_popup.ReconstructionPara.method', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ortho_reconstruction_para', full_name='video_popup.ReconstructionPara.ortho_reconstruction_para', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='persp_reconstruction_para', full_name='video_popup.ReconstructionPara.persp_reconstruction_para', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thresh', full_name='video_popup.ReconstructionPara.thresh', index=3,
      number=101, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=50,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECONSTRUCTIONPARA_RECONSTRUCTIONPIPELINE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2166,
  serialized_end=2632,
)

_PERSPFITTINGPARA.fields_by_name['fh_fitting'].enum_type = _PERSPFITTINGPARA_FHFITTING
_PERSPFITTINGPARA.fields_by_name['fitting_error'].enum_type = _PERSPFITTINGPARA_FITTINGERROR
_PERSPFITTINGPARA_FHFITTING.containing_type = _PERSPFITTINGPARA
_PERSPFITTINGPARA_FITTINGERROR.containing_type = _PERSPFITTINGPARA
_MODELFITTINGPARA_GRAPHCUTPARA.fields_by_name['engine'].enum_type = _MODELFITTINGPARA_GRAPHCUTPARA_ENGINE
_MODELFITTINGPARA_GRAPHCUTPARA.containing_type = _MODELFITTINGPARA
_MODELFITTINGPARA_GRAPHCUTPARA_ENGINE.containing_type = _MODELFITTINGPARA_GRAPHCUTPARA
_MODELFITTINGPARA.fields_by_name['persp_fitting_para'].message_type = _PERSPFITTINGPARA
_MODELFITTINGPARA.fields_by_name['ortho_fitting_para'].message_type = _ORTHOFITTINGPARA
_MODELFITTINGPARA.fields_by_name['subspace_fitting_para'].message_type = _SUBSPACEFITTINGPARA
_MODELFITTINGPARA.fields_by_name['fitting_model'].enum_type = _MODELFITTINGPARA_FITTINGMODEL
_MODELFITTINGPARA.fields_by_name['gric_model_selection_para'].message_type = _GRICMODELSELECTIONPARA
_MODELFITTINGPARA.fields_by_name['graph_cut_para'].message_type = _MODELFITTINGPARA_GRAPHCUTPARA
_MODELFITTINGPARA_FITTINGMODEL.containing_type = _MODELFITTINGPARA
_SEGMENTATIONPARA.fields_by_name['model_fitting_para'].message_type = _MODELFITTINGPARA
_RECONSTRUCTIONPARA.fields_by_name['method'].enum_type = _RECONSTRUCTIONPARA_RECONSTRUCTIONPIPELINE
_RECONSTRUCTIONPARA.fields_by_name['ortho_reconstruction_para'].message_type = _ORTHORECONSTRUCTIONPARA
_RECONSTRUCTIONPARA.fields_by_name['persp_reconstruction_para'].message_type = _PERSPRECONSTRUCTIONPARA
_RECONSTRUCTIONPARA_RECONSTRUCTIONPIPELINE.containing_type = _RECONSTRUCTIONPARA
DESCRIPTOR.message_types_by_name['NeighborhoodPara'] = _NEIGHBORHOODPARA
DESCRIPTOR.message_types_by_name['GRICModelSelectionPara'] = _GRICMODELSELECTIONPARA
DESCRIPTOR.message_types_by_name['PerspFittingPara'] = _PERSPFITTINGPARA
DESCRIPTOR.message_types_by_name['OrthoFittingPara'] = _ORTHOFITTINGPARA
DESCRIPTOR.message_types_by_name['SubspaceFittingPara'] = _SUBSPACEFITTINGPARA
DESCRIPTOR.message_types_by_name['ModelFittingPara'] = _MODELFITTINGPARA
DESCRIPTOR.message_types_by_name['SegmentationPara'] = _SEGMENTATIONPARA
DESCRIPTOR.message_types_by_name['OrthoReconstructionPara'] = _ORTHORECONSTRUCTIONPARA
DESCRIPTOR.message_types_by_name['PerspReconstructionPara'] = _PERSPRECONSTRUCTIONPARA
DESCRIPTOR.message_types_by_name['ReconstructionPara'] = _RECONSTRUCTIONPARA

NeighborhoodPara = _reflection.GeneratedProtocolMessageType('NeighborhoodPara', (_message.Message,), dict(
  DESCRIPTOR = _NEIGHBORHOODPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.NeighborhoodPara)
  ))
_sym_db.RegisterMessage(NeighborhoodPara)

GRICModelSelectionPara = _reflection.GeneratedProtocolMessageType('GRICModelSelectionPara', (_message.Message,), dict(
  DESCRIPTOR = _GRICMODELSELECTIONPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.GRICModelSelectionPara)
  ))
_sym_db.RegisterMessage(GRICModelSelectionPara)

PerspFittingPara = _reflection.GeneratedProtocolMessageType('PerspFittingPara', (_message.Message,), dict(
  DESCRIPTOR = _PERSPFITTINGPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.PerspFittingPara)
  ))
_sym_db.RegisterMessage(PerspFittingPara)

OrthoFittingPara = _reflection.GeneratedProtocolMessageType('OrthoFittingPara', (_message.Message,), dict(
  DESCRIPTOR = _ORTHOFITTINGPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.OrthoFittingPara)
  ))
_sym_db.RegisterMessage(OrthoFittingPara)

SubspaceFittingPara = _reflection.GeneratedProtocolMessageType('SubspaceFittingPara', (_message.Message,), dict(
  DESCRIPTOR = _SUBSPACEFITTINGPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.SubspaceFittingPara)
  ))
_sym_db.RegisterMessage(SubspaceFittingPara)

ModelFittingPara = _reflection.GeneratedProtocolMessageType('ModelFittingPara', (_message.Message,), dict(

  GraphCutPara = _reflection.GeneratedProtocolMessageType('GraphCutPara', (_message.Message,), dict(
    DESCRIPTOR = _MODELFITTINGPARA_GRAPHCUTPARA,
    __module__ = 'video_popup_pb2'
    # @@protoc_insertion_point(class_scope:video_popup.ModelFittingPara.GraphCutPara)
    ))
  ,
  DESCRIPTOR = _MODELFITTINGPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.ModelFittingPara)
  ))
_sym_db.RegisterMessage(ModelFittingPara)
_sym_db.RegisterMessage(ModelFittingPara.GraphCutPara)

SegmentationPara = _reflection.GeneratedProtocolMessageType('SegmentationPara', (_message.Message,), dict(
  DESCRIPTOR = _SEGMENTATIONPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.SegmentationPara)
  ))
_sym_db.RegisterMessage(SegmentationPara)

OrthoReconstructionPara = _reflection.GeneratedProtocolMessageType('OrthoReconstructionPara', (_message.Message,), dict(
  DESCRIPTOR = _ORTHORECONSTRUCTIONPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.OrthoReconstructionPara)
  ))
_sym_db.RegisterMessage(OrthoReconstructionPara)

PerspReconstructionPara = _reflection.GeneratedProtocolMessageType('PerspReconstructionPara', (_message.Message,), dict(
  DESCRIPTOR = _PERSPRECONSTRUCTIONPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.PerspReconstructionPara)
  ))
_sym_db.RegisterMessage(PerspReconstructionPara)

ReconstructionPara = _reflection.GeneratedProtocolMessageType('ReconstructionPara', (_message.Message,), dict(
  DESCRIPTOR = _RECONSTRUCTIONPARA,
  __module__ = 'video_popup_pb2'
  # @@protoc_insertion_point(class_scope:video_popup.ReconstructionPara)
  ))
_sym_db.RegisterMessage(ReconstructionPara)


# @@protoc_insertion_point(module_scope)
