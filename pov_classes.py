#
class Scene:
    def __init__(self):
        self.camera = None
        self.lights = []
        self.objects = []
        
    def add_camera(self, camera):
        self.camera = camera
    
    def add_light(self, light):
        self.lights.append(light)

    def add_object(self, object):
        self.objects.append(object)

    def generate_pov_content(self):
        
        lines = []

        # These are the lines in the header (generalize later)
        lines.append('#include "colors.inc"')
        lines.append('background { color Cyan }')

        # Add camera info
        lines.append('\n// Camera \n')
        lines += self.camera.get_lines()

        # Add light info
        lines.append('\n// Lights \n')
        for light in self.lights:
            lines += light.get_lines()
        
        # Add objects info
        lines.append('\n// Objects \n')
        for object in self.objects:
            lines += object.get_lines()

        # Put it all together
        content = '\n'.join(lines)
        
        return content

    def generate_pov_file(self):

        content = self.generate_pov_content()
        text_file = open("data.pov", "w")
        text_file.write(content)
        text_file.close()
        
        return

class Object:
    pass

class Camera:
    
    def __init__(self, location=(0,1,-2), look_at=(0,0,0)):
        self.location = location
        self.look_at = look_at

    def get_lines(self):
        
        lines = ['camera']
        
        l1 = 'location '+ pov_str_vector(self.location)
        l2 = 'look_at '+ pov_str_vector(self.look_at)
        lines += c_brackets([l1,l2])

        return lines


class Light:
    
    def __init__(self, location=(2,4,-3), color='White'):
        self.location = location
        self.color = color

    def get_lines(self):
        
        lines = ['light_source']
        l1 = pov_str_vector(self.location)+' color White'
        lines += c_brackets([l1])

        return lines


class Sphere(Object):
    
    def __init__(self, 
                 center=(0,0,0), 
                 radius=1, 
                 texture='pigment { color Red }'):
        self.center = center
        self.radius = radius
        self.texture = texture

    def get_lines(self):

        sphere_def = ['\nsphere']
        
        sphere_prop = [pov_str_vector(self.center) +\
                      ', ' + str(self.radius)]
        texture_def = ['texture']+ c_brackets([self.texture])

        sphere_def +=  c_brackets(sphere_prop + texture_def)

        return sphere_def


class Box(Object):
    def __init__(self, 
                 near_lower_left=(1,0,0),
                 far_upper_right=(-1,1,1),
                 texture = 'pigment {color Red}'):
        self.near_lower_left = near_lower_left
        self.far_upper_right = far_upper_right
        self.texture = texture
    
    def get_lines(self):
        
        near_l_l = pov_str_vector(self.near_lower_left)
        far_u_r = pov_str_vector(self.far_upper_right)
        corners = [', '.join([near_l_l,far_u_r])]
        
        texture= ['texture']+ c_brackets([self.texture])
    

        box_def = ['box']+c_brackets(corners + texture)

        return box_def


class Cone(Object):
    def __init__(self, 
                 center_top = (0,0,0),
                 radius_top = 1,
                 center_bottom = (0,0,1),
                 radius_bottom = 2,
                 texture = 'pigment {color Red}'):
        self.center_top = center_top
        self.radius_top = radius_top
        self.center_bottom = center_bottom
        self.radius_bottom = radius_bottom
        self.texture = texture


    def get_lines(self):
        
        center_radius_top = [pov_str_vector(self.center_top)\
                             +', '+ str(self.radius_top)]
        center_radius_bottom = [pov_str_vector(self.center_bottom)\
                             +', '+ str(self.radius_bottom)]
        cone_properties = center_radius_top + center_radius_bottom

        texture_def = ['texture'] + c_brackets([self.texture])
        cone_properties += texture_def

        cone_def = ['cone'] + c_brackets(cone_properties) 

        return cone_def
    
# functions
def pov_str_vector(vector):
    pov_str = '<'+ \
              str(vector[0]) + ', ' + \
              str(vector[1]) + ', ' + \
              str(vector[2]) +'>'
    return pov_str


def c_brackets(lines):
    return ['\t{']+ ['\t'+line for line in lines] + ['\t}']