#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:03:45 2019

@author: ece-student
"""

# Copyright 2019 Dingjun Bian braybian@bu.edu
# Copyright 2019 Shiyang Hu shiyangh@bu.edu
import sys
import numpy as np
import math


class Circle():
    def __init__(self, name, m, R, position, velocity):
        self.name = name
        self.m = m
        self.R = R
        self.pos = position
        self.vel = velocity

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.name, round(self.m,6),
                                                   round(self.R),
                                                   round(self.pos[0], 6),
                                                   round(self.pos[1], 6),
                                                   round(self.pos[2], 6),
                                                   round(self.vel[0], 6),
                                                   round(self.vel[1], 6),
                                                   round(self.vel[2], 6))

    def move(self, movetime):
        #print("before move:",self.pos[0],' ',self.pos[1],' ',self.pos[2])
        self.pos = self.pos + movetime * self.vel  # r=p+tv
        #print("after move:",self.pos[0],' ',self.pos[1],' ',self.pos[2])
        # print("self.pos:",self.pos) ######

    def colli_time(self, two):
        if (self.pos[0]==two.pos[0]) & (self.pos[1]==two.pos[1]) & (self.pos[2]==two.pos[2]):
            return np.Inf
        subr1=self.pos[0]-two.pos[0]
        subr2 = self.pos[1] - two.pos[1]
        subr3 = self.pos[2] - two.pos[2]
        subv1 = self.vel[0] - two.vel[0]
        subv2 = self.vel[1] - two.vel[1]
        subv3 = self.vel[2] - two.vel[2]
        r1 = float(self.R)
        r2 = float(two.R)
        midpro1=subv1*subv1+subv2*subv2+subv3*subv3
        if midpro1 == 0:
            return np.Inf
        dr2=subr1*subr1+subr2*subr2+subr3*subr3
        midpro2=2*subr1*subv1+2*subr2*subv2+2*subr3*subv3
        sqgen=midpro2*midpro2-4*midpro1*(dr2-(r1+r2)**2)
        if sqgen < 0:
            return np.Inf
        root = sqgen ** 0.5
        colltime = (-midpro2 - root) / (2 * midpro1)
        colltime1 = (-midpro2 + root) / (2 * midpro1)
        if (colltime <= 0):
            colltime = colltime1
        if (colltime > 0) & (colltime1 > 0) & (colltime1 < colltime):
            colltime = colltime1
        # print("eralytestcolltime:",colltime)
        if colltime == 0 and (subr1*subv1+subr2*subv2+subr3*subv3) < 0:
            return 0
        elif colltime > 0:
            # print("collitime:",colltime)  ######
            return colltime
        return np.Inf




    def collison_space(self, area):
        tmin = np.Inf
        # print("a1 b1 c1:",a1,b1,c1)
        if (self.vel[0]==0) & (self.vel[1]==0) & (self.vel[2]==0):
            pass
        else:
            a = (self.vel[0] ** 2) + (self.vel[1] ** 2 )+ (self.vel[2] ** 2)
            b = (2 * self.vel[0] * self.pos[0]) + (2 * self.vel[1] * self.pos[1]) + (2 * self.vel[2] * self.pos[2])
            c = (self.pos[0] ** 2) + (self.pos[1] ** 2) + (self.pos[2] ** 2) - ((area-float(self.R)) ** 2)
            sq =( b ** 2) -( 4 * a * c)
            if sq < 0:
                return 1
            sqgen = sq ** 0.5
            # print("sq:",sq,"sqgen:",sqgen,"b:",b,"a:",a,"c:",c)
            t_mid = (-b - sqgen) / (2 * a)
            t_mid2 = (-b + sqgen) / (2 * a)
            # print("b sqgen a:",b,sqgen,a)
            # print("t_mid:",t_mid,t_mid2)
            if (t_mid < tmin) & (t_mid > 0):
                tmin = t_mid
            if (t_mid2 < tmin) & (t_mid2 > 0):
                tmin = t_mid2
            # print("collision space tmin:",tmin)
            # print("t1:", t1, "t2", t2, "tmin", tmin)
        return tmin


def get_argvin():
    n_times = sys.argv[2]
    global area
    area = sys.argv[1]
    return area, n_times


def get_circle_data(n_times,area):
    circles = []
    momentum = np.zeros(3)
    energy = 0
    st_gtd = 'Here are the initial spheres.\n'
    st_gtd=st_gtd+"universe radius "+str(area)+"\n"+"max collsions "+str(n_times)+"\n"
    for line in sys.stdin:
        try:
            m, R, posx, posy, posz, velx, vely, velz, name = line.split()
            # name, posx, posy, velx, vely = line.split()
            # print(name,posx,posy,velx,vely)
            pos = np.array((float(posx), float(posy), float(posz)))
            vel = np.array((float(velx), float(vely), float(velz)))
            circles.append(Circle(name, m, R, pos, vel))
            momentum = momentum + int(m) * vel
            # print("momentum:",momentum)
            energy = energy + int(m) * vel @ vel / 2
            # print("energy:",energy)
            st_gtd = st_gtd+ str(name) + " m=" + str(m) + " R=" + str(R) + " p=" + str(pos) + " v=" + str(vel) + " bounce=0\n"
        except ValueError:
            return None
    st_gtd = st_gtd + "energy: " + str(energy) + "\nmomentum: " + str(momentum)
    #print("universe radius ", area)
    #print("max collision ", n_times)
    print(st_gtd)
    # print("the first circle:", circles[0], circles[0].vel, len(circles))
    return circles


def get_next_collision(cur_time, circles,bounce):
    next_collision = np.Inf
    colliders = [None, None]
    collide4 = [None, None, None, None]
    global divide
    divide = 1
    for i, one in enumerate(circles):
        # print("i:",i,"one:",one)      #######
        for j, two in enumerate(circles):
            # print("j:",j,"two:",two)     #####
            # print("type of j:",type(j))
            if i >= j:  # make sure it is two different balls
                continue
            colltime = one.colli_time(two)
            # print("colltime",colltime)
            if colltime < next_collision:
                next_collision = colltime
                colliders = i, j
                collide4[0] = i
                collide4[1] = j
            elif (colltime == next_collision) & (colltime < np.Inf) & (collide4[0] != None):
                collide4[2] = i
                collide4[3] = j
                # print("new i j:",i,j)
                # print("collide4:",collide4)
                divide = 2
                # print("type of colliders:", type(colliders))
    if divide == 1:
        #bounce[i]=bounce[i]+1

        return colliders, next_collision, divide  # no collision for given time
    elif divide == 2:
        return collide4, next_collision, divide


def move_ball(circles, movetime):
    for circ in circles:
        circ.move(movetime)


def collision_report(cur_time, one,two,circles, bounce):
    str_col = ""
    ener=0
    moment=0
    str_col = str_col + "time of the event:" + str(cur_time) + "\n"
    str_col = str_col + "colliding " + str(one.name) + " " + str(two.name) + "\n"
    for i in range(len(circles)):
      str_col = str_col + str(circles[i].name) + " m=" + str(circles[i].m) + " R=" + str(circles[i].R) + " p=" + str(circles[i].pos) + " v=" + str(
        circles[i].vel) +" bounce="+str(bounce[i])+"\n"
    #str_col = str_col + str(two.name) + " m=" + str(two.m) + " R=" + str(two.R) + " p=" + str(two.pos) + " v=" + str(
    #    two.vel) + " bounce="+bounce[i]+"\n"
    for i in range(len((circles))):
      ener =ener+ float(circles[i].m) * circles[i].vel @ circles[i].vel / 2
      moment =moment+ float(circles[i].m) * circles[i].vel
    # print("energy:",ener)  #####
    # print("momentum:",moment) #####
    str_col = str_col + "energy: " + str(ener) + "\nmomentum: " + str(moment)
    print(str_col)


def collision_wall_report(cur_time, one,circles,bounce):
    str_col = ""
    ener=0
    moment=0
    str_col = str_col + "time of the event:" + str(cur_time) + "\n"
    str_col = str_col + "reflecting " + str(one.name) +"\n"
    for i in range(len(circles)):
      str_col = str_col + str(circles[i].name) + " m=" + str(circles[i].m) + " R=" + str(circles[i].R) + " p=" + str(circles[i].pos) + " v=" + str(
        circles[i].vel) +"bounce "+str(bounce[i])+"\n"
    for i in range(len(circles)):
      ener =ener+ float(circles[i].m) * circles[i].vel @ circles[i].vel / 2
      moment =moment+ float(circles[i].m) * circles[i].vel
    # print("energy:",ener)  #####
    # print("momentum:",moment) #####
    str_col = str_col + "energy: " + str(ener) + "\nmomentum: " + str(moment)
    print(str_col)


def elastic_collision(one, two):
    one.m = float(one.m)
    two.m = float(two.m)
    posub=[one.pos[0]-two.pos[0],one.pos[1]-two.pos[1],one.pos[2]-two.pos[2]]
    velsub=[one.vel[0]-two.vel[0],one.vel[1]-two.vel[1],one.vel[2]-two.vel[2]]
    ppmul=posub[0]*posub[0]+posub[1]*posub[1]+posub[2]*posub[2]
    vpmul=velsub[0]*posub[0]+velsub[1]*posub[1]+velsub[2]*posub[2]
    massmul1 = (2 * two.m) / (one.m + two.m)
    massmul2 = (2 * one.m) / (one.m + two.m)
    one.vel[0]=one.vel[0]-massmul1*(posub[0]*vpmul/ppmul)
    one.vel[1] = one.vel[1] - massmul1 * (posub[1] * vpmul / ppmul)
    one.vel[2] = one.vel[2] - massmul1 * (posub[2] * vpmul / ppmul)
    two.vel[0] = two.vel[0] + massmul2 * (posub[0] * vpmul / ppmul)
    two.vel[1] = two.vel[1] + massmul2 * (posub[1] * vpmul / ppmul)
    two.vel[2] = two.vel[2] + massmul2 * (posub[2] * vpmul / ppmul)







def collisonspace_vel(one, area):  ########## nead modify
    # one.vel=-one.vel
    # area=float(area)
    wall = np.array((0, 0, 0))
    # print(wall)
    # print(one.pos)
    mid = one.pos - wall
    # print("one.m:",one.m,"two.m:",two.m)  #####
    sub = 2 * (one.vel) @ mid / (mid @ mid)
    one.vel = one.vel - sub * mid


def main():
    print(   "Please enter the mass, radius, x/y/z position, x/y/z velocity and name of each sphere When complete, use EOF / Ctrl-D to stop entering")
    area, n_times = get_argvin()   #n_times=max time of collison for one ball
    n_times = int(n_times)
    area = float(area)
    circles = get_circle_data(n_times,area)  # get the data of the circle
    #print("Here are the initial conditions.")
    global bounce;
    bounce=[0]*len(circles)
    #print("initial bounce",bounce)
    #bounce1=0
    #bounce2=0
    #bounce3=0


    if not circles:
        return 1
    seperate = 0
    cur_time = 0  # init time=0
    collide = [0, 0, 0, 0]
    while len(circles)>0:

          (collide), c_time, divide = get_next_collision(cur_time, circles,bounce)  # if no collision c_time=inf
          seperate = 0
          if divide == 1:
             one = collide[0]
             two = collide[1]
          if divide == 2:
             one = collide[0]
             two = collide[1]
             three = collide[2]
             four = collide[3]
          # print("c_time", c_time)
          lop_cir = 0  # for the loop
          tmin = 9999
          numb = 0
          tmid_list = []  # store the shortest time of collision with wall of each ball
          for lop_cir in circles:  # get the shortest time of hit the wall
             t_mid = lop_cir.collison_space(area)
             tmid_list.append(t_mid)
             #print("t_mid:",t_mid)
          for lop_min in range(len(tmid_list)):  # get the shortest of the shortest(hit wall)
             if tmid_list[lop_min] < tmin:
                 tmin = tmid_list[lop_min]
                 numb = lop_min
                 #print("tmid_list[lop_min]:",tmid_list[lop_min]," numb:",numb)

          if tmin < c_time:  # set to deal with hit the wall
             c_time = tmin
             seperate = 1

          cur_time = cur_time + c_time
          # print("current_time:", cur_time)
          move_ball(circles, c_time)  # when c_time<the required to times,go to this point
          if seperate == 0:
              elastic_collision(circles[one], circles[two])  # change the velocity
              if divide == 2:
                 elastic_collision(circles[three], circles[four])
          elif seperate == 1:
              #print("numb:",numb,len(circles),'\n')
              collisonspace_vel(circles[numb], area)  # change the velocity
              # print(circles[numb].vel)

          for it in range(len(circles)):    #if one of the vel euals to nan,return o
              if (math.isnan(circles[it].vel[0])) | (math.isnan(circles[it].vel[0]))  | (math.isnan(circles[it].vel[0])):
                  return 0


          if seperate == 0:
            bounce[one] = bounce[one] + 1
            bounce[two] = bounce[two] + 1
            collision_report(cur_time, circles[one],circles[two],circles,bounce)
            if divide == 2:
                     bounce[three] = bounce[three] + 1
                     bounce[four] = bounce[four] + 1
                     collision_report(cur_time,  circles[three],circles[four],circles,bounce)
          elif seperate == 1:  # next collision is hitting the wall
              # print("hit the wall")  ####
              bounce[numb] = bounce[numb] + 1
              collision_wall_report(cur_time,circles[numb], circles,bounce)
              #n_times = n_times - 1
          tinymove= 0.000001
          cur_time = cur_time + tinymove # avoid counting one collison twice
          move_ball(circles, tinymove)
          #print("len circle",len(circles),len(bounce))
          i=len(circles)-1
          while i>=0:
             if bounce[i]==int(n_times):      #check whether we should delete the ball
                 print("disappear ", circles[i].name)
                 del circles[i]
                 del bounce[i]
                 #deln=deln-1
             i=i-1
    else:
       return 0


if __name__ == '__main__':
    main()





