
class Scene:
    def __init__(self):
        self.camera = None
        self.lights = []
        self.objects = []
        
    def add_camera(self, camera):
        self.camera = camera

    def add_light(self, light):
        self.lights.append(light)
        
    def add_sphere(self, sphere):
        self.objects.append(sphere)
    
    def display(self):

        print ('Camera')
        camera = self.camera

        if camera==None:
            print('No camera defined')
        else:
            camera.display()
        
        print('Lights')
        for light in self.lights:
            light.display()
            
        print('Objects')
        for object in self.objects:
            object.display()

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

class Camera:
    
    def __init__(self, location=(0,1,-2), look_at=(0,0,0)):
        self.location = location
        self.look_at = look_at
    
    def display(self):
        print('\t','Location: ', self.location)
        print('\t','Look at: ', self.look_at)
        print()

    def get_lines(self):
        
        lines = []
        
        lines.append('camera {')
        lines.append('location '+ pov_str_vector(self.location))
        lines.append('look_at '+ pov_str_vector(self.look_at))
        lines.append('}')

        return lines

class Light:
    
    def __init__(self, location=(2,4,-3), color='White'):
        self.location = location
        self.color = color
    
    def display(self):
        print('\t','location: ', self.location)
        print('\t','color: ', self.color)
        print()

    def get_lines(self):
        
        lines = []
        
        lines.append('light_source {')
        lines.append( pov_str_vector(self.location)+' color White')
        lines.append('}')

        return lines

class Sphere:
    
    def __init__(self, center=(0,0,0), radius=1, texture='pigment { color Red }'):
        self.center = center
        self.radius = radius
        self.texture = texture
        
    def display(self):
        print('Sphere')
        print('\t', 'center: ', self.center)
        print('\t','radius: ', self.radius)
        print('\t','texture: ', self.texture)
        print()

    def get_lines(self):
        
        lines = []
        
        lines.append('sphere {')
        lines.append( pov_str_vector(self.center)+\
                      ', ' + \
                      str(self.radius))
        lines.append('texture {')
        lines.append(self.texture)
        lines.append('}')

        lines.append('}')

        return lines

def pov_str_vector(vector):
    pov_str = '<'+ \
              str(vector[0]) + ',' + \
              str(vector[1]) + ',' + \
              str(vector[2]) +'>'
    return pov_str