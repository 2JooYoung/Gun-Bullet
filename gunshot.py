import maya.cmds as cmds
 class Gun:
    def __init__(self, barrelLength=1, handleLength=0.5):
       
        self.barrel = cmds.polyCube(w=barrelLength, h=0.2, d=0.2)[0]
        cmds.move(barrelLength / 2, 0, 0)  
     
        self.handle = cmds.polyCube(w=0.2, h=handleLength, d=0.2)[0]
        cmds.move(0, -handleLength / 2, 0)  
    
        self.triggerGuard = cmds.polyCylinder(r=0.1, h=0.05)[0]
        cmds.rotate(0, '90deg', 0)
        cmds.move(0.1, -0.2, 0)  
   
        cmds.parent(self.handle, self.barrel)
        cmds.parent(self.triggerGuard, self.barrel)
    
        self.gun = cmds.polyUnite(self.barrel, self.handle, self.triggerGuard, 
n='Gun')[0]
     
        self.bullet = cmds.polySphere(r=0.1)[0]
        cmds.hide(self.bullet)
    def aim(self, target):
        cmds.aimConstraint(target, self.gun, aimVector=(1, 0, 0))
        cmds.aimConstraint(target, self.gun, e=True, remove=True)
    def shoot(self, targetName):
        if not cmds.objExists(targetName):
            print(f"Target '{targetName}' does not exist.")
            return
        targetPos = cmds.xform(targetName, q=True, ws=True, t=True)
        cmds.move(targetPos[0], targetPos[1], targetPos[2], self.bullet)
        cmds.showHidden(self.bullet)
cmds.delete(targetName)
 gun = Gun(barrelLength=3, handleLength=1.5)
 gun.aim('target') 
gun.shoot('pTorus1')  