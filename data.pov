#include "colors.inc"
background { color Cyan }

// Camera 

camera {
location <0,8,-12>
look_at <0,1,2>
}

// Lights 

light_source {
<2,4,-3> color White
}

// Objects 

sphere {
<0,1,2>, 2
texture {
pigment { color Yellow }
}
}
sphere {
<0,-1,-2>, 1
texture {
pigment { color Red }
}
}