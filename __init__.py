'''
Created by Retrax

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Pivot Operators",
    "description": "Pivot point editor",
    "author": "Retrax",
    "version": (0, 0, 1),
    "blender": (2, 78, 0),
    "location": '3D View > Tool Shelf',
    "warning": "The Bug is funny",
    "category": "Object" }
    
import bpy

class PositiveX(bpy.types.Operator):  
    bl_idname = "pivot.xp_operator"
    bl_label = "Pivot X+"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
  
    def execute(self, context):
        
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.x
                 init=1
             elif x.co.x>a:
                 a=x.co.x
                 
        for x in o.data.vertices:
             x.co.x-=a

        o.location.x+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'} 

class NegativeX(bpy.types.Operator):  
    bl_idname = "pivot.xn_operator"
    bl_label = "Pivot X-"    
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.x
                 init=1
             elif x.co.x<a:
                 a=x.co.x
                 
        for x in o.data.vertices:
             x.co.x-=a

        o.location.x+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'}

class PositiveY(bpy.types.Operator):  
    bl_idname = "pivot.yp_operator"
    bl_label = "Pivot Y+"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.y
                 init=1
             elif x.co.y>a:
                 a=x.co.y
                 
        for x in o.data.vertices:
             x.co.y-=a

        o.location.y+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'} 

class NegativeY(bpy.types.Operator):  
    bl_idname = "pivot.yn_operator"
    bl_label = "Pivot Y-"    
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.y
                 init=1
             elif x.co.y<a:
                 a=x.co.y
                 
        for x in o.data.vertices:
             x.co.y-=a

        o.location.y+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'}

class PositiveZ(bpy.types.Operator):  
    bl_idname = "pivot.zp_operator"
    bl_label = "Pivot Z+"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.z
                 init=1
             elif x.co.z>a:
                 a=x.co.z
                 
        for x in o.data.vertices:
             x.co.z-=a

        o.location.z+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'} 

class NegativeZ(bpy.types.Operator):  
    bl_idname = "pivot.zn_operator"
    bl_label = "Pivot Z-"    
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None)
  
    def execute(self, context):
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        o=bpy.context.active_object
        init=0
        for x in o.data.vertices:
             if init==0:
                 a=x.co.z
                 init=1
             elif x.co.z<a:
                 a=x.co.z
                 
        for x in o.data.vertices:
             x.co.z-=a

        o.location.z+=a 
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'}


class Pivotpanel(bpy.types.Panel):
    bl_idname = "pivotpanel"
    bl_label = "Pivotpanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
    
    @classmethod
    def poll(cls, context):
        return (context.object is not None)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        if bpy.context.object is not None:
            row = col.row(align=True)
            row.scale_x=2.0
            row.scale_y=2.0
            row.operator("pivot.xp_operator", text="X+")
            row.operator("pivot.yp_operator", text="Y+")
            row.operator("pivot.zp_operator", text="Z+")
            row = col.row(align=True)
            row.scale_x=2.0
            row.scale_y=2.0
            row.operator("pivot.xn_operator", text="X-")
            row.operator("pivot.yn_operator", text="Y-")
            row.operator("pivot.zn_operator", text="Z-")
            row = col.row(align=True)
            row.alignment='CENTER'
            row.label("Select your object first")
            row = col.row(align=True)
            row.alignment='CENTER'
            row.label("or else the results will")
            row = col.row(align=True)
            row.alignment='CENTER'
            row.label("not be as expected.")
            row = col.row(align=True)
            row.alignment='CENTER'
            row.label("This bug interestingly moves")
            row = col.row(align=True)
            row.alignment='CENTER'
            row.label("the pivot to the corners")
            row = col.row(align=True)
            row.alignment='CENTER'
            row.label("of the object")
        
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()