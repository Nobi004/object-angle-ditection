import cv2
import numpy as np


def find_object(image):
    # Object detection code goes here
    # For demonstration, let's assume object is detected and its bounding box is obtained
    # bounding_box = [x, y, width, height]
    bounding_box = [100, 100, 200, 200]  # Format: [x, y, width, height]
    # Center point calculation
    center_x = bounding_box[0] + bounding_box[2] // 2
    center_y = bounding_box[1] + bounding_box[3] // 2
    return center_x, center_y


def draw_lines(image, center_x, center_y):
    # Draw line 1 (vertical divider line passing through center)
    cv2.line(image, (center_x, 0), (center_x, image.shape[0]), (0, 255, 0), 2)

    # Draw line 2 (xox' axis line passing through center)
    cv2.line(image, (0, center_y), (image.shape[1], center_y), (0, 255, 0), 2)


def calculate_slope(point1, point2):
    return (point2[1] - point1[1]) / (point2[0] - point1[0])


def calculate_angle(m1, m2):
    tan_theta = abs((m2 - m1) / (1 - m1 * m2))
    return np.arctan(tan_theta) * 180 / np.pi


def main():
    # Read image
    image = cv2.imread('sample1.jpg')

    # Find object and center point
    center_x, center_y = find_object(image)

    # Draw lines
    draw_lines(image, center_x, center_y)

    # Define points for slope calculation
    point1 = (center_x, 0)
    point2 = (center_x, image.shape[0])
    point3 = (0, center_y)
    point4 = (image.shape[1], center_y)

    def calculate_slope(point1, point2):
        if point2[0] - point1[0] != 0:
            return (point2[1] - point1[1]) / (point2[0] - point1[0])
        else:
            return float('inf')  # Return infinity to represent vertical line

    # Calculate slopes
    m1 = calculate_slope(point1, point2)
    m2 = calculate_slope(point3, point4)

    # Calculate angle
    angle = calculate_angle(m1, m2)

    print("Angle between lines l1 and l2:", angle)

    # Display image with lines
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
