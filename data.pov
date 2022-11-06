#include "colors.inc"
background { color Cyan }

// Camera 

camera
	{
	location <4, 8, -12>
	look_at <0, 1, 2>
	}

// Lights 

light_source
	{
	<2, 4, -3> color White
	}

// Objects 


sphere
	{
	<0.0, 1.0, 2.0>, 0.7
		{
		texture
			{
			pigment { color Yellow }
			}
		}
	}

sphere
	{
	<0.5, 1.3, 2.4>, 0.8999999999999999
		{
		texture
			{
			pigment { color Yellow }
			}
		}
	}

sphere
	{
	<1.0, 1.6, 2.8>, 1.1
		{
		texture
			{
			pigment { color Yellow }
			}
		}
	}

box
{
<1, 0, 0>,
<-1, 1, 1>
texture
	{
	pigment {color Red}
	}
}