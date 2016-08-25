# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import SpaceTimeRealigner


def test_SpaceTimeRealigner_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(mandatory=True,
    min_ver='0.4.0.dev',
    ),
    slice_info=dict(requires=[u'slice_times'],
    ),
    slice_times=dict(),
    tr=dict(requires=[u'slice_times'],
    ),
    )
    inputs = SpaceTimeRealigner.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_SpaceTimeRealigner_outputs():
    output_map = dict(out_file=dict(),
    par_file=dict(),
    )
    outputs = SpaceTimeRealigner.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
