


'''
Dump of any blender object
'''
def dump(obj):
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))



'''
Context proper overriding
'''

import bpy
from contextlib import contextmanager

@contextmanager
def contextoverride(area_type: str):
    area = bpy.context.area
    former_area_type = area.type
    area.type = area_type
    try:
        yield area
    finally:
        area.type = former_area_type




'''
Detects if object has a previously inserted keyframe on N-frame 

'''
def has_key_frame(ob, frame):
    if ob.animation_data.action and ob.animation_data.action.fcurves :
        for curve in ob.animation_data.action.fcurves:
            for pt in curve.keyframe_points:
                return pt.co[0] == frame 

# if has_key_frame(obj, bpy.context.scene.frame_current) :
    # obj.keyframe_delete(data_path = 'location')