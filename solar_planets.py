import cv2
import numpy as np

# Create a blank canvas for the poster
canvas = np.zeros((800, 1000, 3), dtype=np.uint8)

# Define the names of the planets
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Define the positions for the planet names
name_positions = [(50, 100), (50, 200), (50, 300), (50, 400), (50, 500), (50, 600), (50, 700), (50, 800)]

# Define the color and font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_color = (255, 255, 255)
font_thickness = 3

# Add planet names to the canvas
for i, name in enumerate(planet_names):
    cv2.putText(canvas, name, name_positions[i], font, font_scale, font_color, font_thickness)

# Display the poster
cv2.imshow("Solar System Poster", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the poster to a file
cv2.imwrite("solar_system_poster.png", canvas)
