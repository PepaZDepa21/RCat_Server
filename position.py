import json
from math import sin, cos, radians


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = 0

    def performRequest(self, request):
        try:
            requestDict = json.loads(request)
            if "Rotation" in requestDict and requestDict["Movement"] == 0:
                self.rotate(requestDict["Rotation"], requestDict["Sensitivity"])
            elif "Rotation" in requestDict and requestDict["Movement"] != 0:
                self.move(requestDict["Movement"])
            elif "Name" in requestDict:
                self.action(requestDict["Name"], requestDict["Description"])
        except:
            pass

    def rotate(self, degrees, sensitivity):
        if self.rotation < degrees and self.rotation <= 89 and degrees >= 270:
            self.rotation = degrees
            print(f"X: {self.x} (0); Y: {self.y} (0); Rotation: {self.rotation}° ({-sensitivity})")
        else:
            self.rotation = degrees
            print(f"X: {self.x} (0); Y: {self.y} (0); Rotation: {self.rotation}° ({sensitivity})")


    def move(self, length):
        if self.rotation == 30 or self.rotation == 150:
            changeX = length * 0.5
            changeY = round(length * cos(radians(self.rotation)), 2)
        elif self.rotation == 210 or self.rotation == 330:
            changeX = length * -0.5
            changeY = round(length * cos(radians(self.rotation)), 2)
        elif self.rotation == 60 or self.rotation == 300:
            changeX = round(length * sin(radians(self.rotation)), 2)
            changeY = length * 0.5
        elif self.rotation == 120 or self.rotation == 240:
            changeX = round(length * sin(radians(self.rotation)), 2)
            changeY = length * -0.5
        elif self.rotation == 180:
            changeX = 0
            changeY = -length
        elif self.rotation == 90:
            changeX = length
            changeY = 0
        elif self.rotation == 270:
            changeX = -length
            changeY = 0
        else:
            changeX = round(length * sin(radians(self.rotation)), 2)
            changeY = round(length * cos(radians(self.rotation)), 2)

        self.x += changeX
        self.y += changeY

        print(f"X: {self.x} ({changeX}); Y: {self.y} ({changeY}); Rotation: {self.rotation}° (0)")

    def action(self, name, description):
        print(f"""X: {self.x} (0); Y: {self.y} (0); Rotation: {self.rotation}° (0)
Action {name} successfully performed!
Action description:
{description}
""")
