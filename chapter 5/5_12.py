#Racetrack
import numpy as np
import os
import time
import matplotlib.pyplot as plt

def argMaxLastNAxes(arr, N):
    s = arr.shape
    new_shp = s[:-N] + (np.prod(s[-N:]),)
    max_idx = arr.reshape(new_shp).argmax(-1)
    return np.unravel_index(max_idx, s[-N:])

class RaceTrack:
    def __init__(self, episodeDuration = 20, velocityLimit = (5, 5), stepReward = -1) -> None:
        self.createTrack()
        self.T = episodeDuration
        self.xVelRange = [-1, 1]
        self.yVelRange = [-1, 1]
        self.Q = np.zeros((*self.track.shape, self.xVelRange[-1] - self.xVelRange[0] + 1, self.yVelRange[-1] - self.yVelRange[0] + 1))
        self.vel = [0, 0]
        self.velocityLimit = velocityLimit
        self.stepReward = stepReward
        self.count = np.zeros_like(self.Q)
        self.pos = [0, 0]
        
    def createTrack(self):
        track = np.zeros((32,17), dtype=np.int8)
        #make boundaries
        track[6:, 10:] = -1
        track[7:, 9] = -1
        track[:3, :2] = -1
        track[0, 2] = -1
        track[3, 0] = -1
        track[14:, 0] = -1
        track[15:, 1] = -1
        track[16:, 2] = -1
        self.track = track
        self.startingLine = [[31,3], [31, 8]]
        self.finishLine = [[0, 16], [5, 16]]
        
    def evaluatePolicy(self):
        self.policy = argMaxLastNAxes(self.Q, 2)
    
    def sampleData(self):
        #starting point:
        self.vel = [0, 0]
        self.sampleStartingPoint()
        states = []
        actions = []
        rewards = []
        
        for _ in range(self.T):
            states.append(self.pos)
            self.draw()
            xVelInc, yVelInc = self.sampleAction()
                
            actions.append([xVelInc + 1, yVelInc + 1])
                
            self.vel[0] += xVelInc
            self.vel[1] += yVelInc
            
            if self.doesIntersect():
                rewards.append(0)
                return states, actions, rewards
            
            rewards.append(self.stepReward)
            
            if self.outOfBounds() or self.notOnTrack():
                self.sampleStartingPoint()
                self.vel = [0, 0]
                continue
            
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]
        
    def sampleStartingPoint(self):
        self.pos = [np.random.randint(self.startingLine[0][0], self.startingLine[1][0]+1), np.random.randint(self.startingLine[0][1], self.startingLine[1][1]+1)]
    
    def sampleAction(self):
        xVelInc = 0
        yVelInc = 0
        newXVel = self.vel[0] + xVelInc
        newYVel = self.vel[1] + yVelInc
        velNorm = np.linalg.norm([newXVel, newYVel])
        firstEntrance = True
        while not (0 < velNorm <= np.sqrt(2 * 16)) or not (-5 < newXVel <= 0) or not (0 <= newYVel < 5) or newXVel * newYVel == 0 or firstEntrance:
            xVelInc = np.random.randint(self.xVelRange[0], self.xVelRange[1] + 1)
            yVelInc = np.random.randint(self.yVelRange[0], self.yVelRange[1] + 1)
            
            newXVel = self.vel[0] + xVelInc
            newYVel = self.vel[1] + yVelInc
            velNorm = np.linalg.norm([newXVel, newYVel])
            firstEntrance = False
            
        return xVelInc, yVelInc
        
    def notOnTrack(self):    
        x1 = min(self.pos[0], self.pos[0] + self.vel[0])
        x2 = max(self.pos[0], self.pos[0] + self.vel[0])
        y1 = min(self.pos[1], self.pos[1] + self.vel[1])
        y2 = max(self.pos[1], self.pos[1] + self.vel[1])
        return (self.track[x1 : x2 + 1,y1:y2+1] == -1).any()
        
    def outOfBounds(self):
        return not (0 <= self.pos[0] + self.vel[0] < self.track.shape[0] and 0 <= self.pos[1] + self.vel[1] < self.track.shape[1])
        
    def doesIntersect(self):
        y_min = min(self.pos[1], self.pos[1] + self.vel[1])
        y_max = max(self.pos[1], self.pos[1] + self.vel[1])
        
        x_max = max(self.pos[0], self.pos[0] + self.vel[0])
        x_min = min(self.pos[0], self.pos[0] + self.vel[0])
        
        return x_min <= self.finishLine[0][0] <= x_max and (y_min <= self.finishLine[0][1] <= y_max or y_min <= self.finishLine[1][1] <= y_max)
        
    def draw(self):
        img = self.track.copy()
        img[self.pos[0], self.pos[1]] = 8
        plt.imshow(img)
        plt.pause(1)        
        
exp = RaceTrack()
plt.ion()
exp.sampleData()