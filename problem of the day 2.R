
s1=c(-10,20,-10,-18)
s2=c(-10,20,0,3)
s3=c(0,3,8,17)
s4=c(8,17,10,-16)
s5=c(10,-16,-10,-18)
 # creating matrix
m=rbind(s1, s2, s3,s4,s5)
print(m)


#find the length
new_m=(m[, c(3, 4)]-m[,c(1,2)])^2
new_m=new_m[,1]+new_m[,2]
L=sqrt(new_m)
L

#slope
S=(m[,4]-m[,2])/(m[,3]-m[,1])
S
Output_m=cbind(L,S)
Output_m=round(Output_m, digits = 1)
Output_m

columns= m[, c(2, 4)]
print(max(columns))
print(min(columns))