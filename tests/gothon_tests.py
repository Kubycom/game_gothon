from nose.tools import *
from game import gothon


def test_engine_map():
    map = gothon.Map('central_corridor')
    engine = gothon.Engine(map)
    assert_equal(engine.scene_map, map)
    # current scene/first scene
    assert_equal(engine.scene_map.opening_scene(), map.opening_scene())
    assert_equal(map.opening_scene(), map.scenes.get('central_corridor'))
    # last scene
    assert_equal(map.next_scene('finished'), map.scenes.get('finished'))


def test_map():
    map = gothon.Map('central_corridor')
    assert_equal(map.start_scene, 'central_corridor')

    centrall_corridor = gothon.CentralCorridor()
    assert_equal(map.next_scene('central_corridor'), map.scenes['central_corridor'])
    assert_equal(map.scenes.get('central_corridor'), map.scenes['central_corridor'])
