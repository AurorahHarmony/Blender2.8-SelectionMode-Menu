import bpy
from bpy.types import Menu, Operator

class WireMode(Operator):
    bl_idname = "wire.mode"
    bl_label = "WireMode"

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'WIREFRAME'
                        
        return {'FINISHED'}
		
class SolidMode(Operator):
    bl_idname = "solid.mode"
    bl_label = "SolidMode"

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        
        return {'FINISHED'}
    
class RenderedMode(Operator):
    bl_idname = "rendered.mode"
    bl_label = "RenderedMode"

    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'RENDERED'
                        
        return {'FINISHED'}
		

class Pie_MT_SelectionMode(Menu):
    bl_label = "Selection Mode"
    bl_idname = "PIE_MT_SELECTIONMODE"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("mesh.select_mode", text="Vertex", icon='VERTEXSEL').type = 'VERT'
        pie.operator("mesh.select_mode", text="Face", icon='FACESEL').type = 'FACE'
        pie.operator("solid.mode", text="Solid", icon="SHADING_SOLID")
        pie.operator("mesh.select_mode", text="Edge", icon='EDGESEL').type = 'EDGE'
        pie.operator("object.mode_set", text="Object", icon='OBJECT_DATAMODE').mode = 'OBJECT'
        pie.operator("object.mode_set", text="Edit", icon='EDITMODE_HLT').mode = 'EDIT'
        pie.operator("wire.mode", text="Wireframe", icon="SHADING_WIRE")
        pie.operator("rendered.mode", text="Rendered", icon="SHADING_RENDERED")

def register():
    bpy.utils.register_class(Pie_MT_SelectionMode)
    bpy.utils.register_class(WireMode)
    bpy.utils.register_class(SolidMode)
    bpy.utils.register_class(RenderedMode)
	
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new("wm.call_menu_pie", "RIGHTMOUSE", "PRESS").properties.name = "PIE_MT_SELECTIONMODE"

def unregister():
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new("wm.call_menu_pie", "RIGHTMOUSE", "PRESS").properties.name = "PIE_MT_SELECTIONMODE"
	
    bpy.utils.unregister_class(RenderedMode)
    bpy.utils.unregister_class(SolidMode)
    bpy.utils.unregister_class(WireMode)
    bpy.utils.unregister_class(Pie_MT_SelectionMode)

if __name__ == "__main__":
    register()

    bpy.ops.wm.call_menu_pie(name="Pie_MT_SelectionMode")
	
	
bl_info = {
    "name": "Selection Mode Pie",
    "author": "Aurorah - Scriptronix Studios",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "description": "A Pie menu that allows you to select your selection and view modes",
    "category": "User Interface"
}