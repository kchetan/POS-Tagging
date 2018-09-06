import math
import sys
import os
import re

#-------------------------------------------- TAGS FROM TAGSET ----------------------------------------------------
f1=open("../src/TagSet.txt","r")
tagset={}
emission={}
unigrams=0
transmission={}
array=[]

for line in f1:
	line=line.replace('\n','')
	if line!='':
		tagset[line]=0

tags=tagset.copy()

for i in tags.keys():
	transmission[i]=tags.copy()

transmission['start']=tags.copy()

#----------------------------------------------- MORPH ANALYSIS FOR TRAINING DATA  ------------------------------------------------------
nouns={}
f1.close()
os.system("fst-compiler ../src/telugu_multiple.fst ../src/telugu_multiple.a ")
f1=open("../src/telugu_pos_wx.txt","r")
f2=open("../src/telugu_morphed.txt","w")
for line in f1:
	line=line.replace('\n','')
	if line!='':
		line=line.split(' ')
		a=line[2:-1]
		b=[]
		for i in range(len(a)):
			w=a[i].split('_')
			if len(w)==2:
				if w[1]=="NN" or w[1]=="NNS":
					try:
						b.append(noun[w[0]]+'_'+w[1])
					except:
						f5=open("../src/multiplelex","w")
						f5.write(w[0])
						f5.close()
						os.system("fst-parse ../src/telugu_multiple.a ../src/multiplelex > ../src/out")
						f5=open("../src/out","r")
						for j in f5:
							if j.find('analysis')!=-1:
								nouns[w[0]]=w[0]
								b.append(a[i])
							else:
								j=j.split('<')[0]
								nouns[w[0]]=j
								b.append(j+'_'+w[1])
							break
						f5.close()
				else:
					b.append(a[i])
			else:
				b.append(a[i])
		b=line[:2]+b+[line[-1]]
		b=' '.join(b)
		f2.write(b+'\n')
f2.close()
f1.close()
#print nouns
f1=open(sys.argv[1],"r")
f2=open("../src/telugu_test_morphed.txt","w")
#----------------------------------------- MORPH FOR TEST DATA ------------------------------------------------------
for line in f1:
	line=line.replace('\n','')
	if line!='':
		line=line.split(' ')
		a=line[2:-1]
		b=[]
		for i in range(len(a)):
			try:
				b.append(noun[w[0]]+'_'+w[1])
			except:
				f5=open("../src/multiplelex","w")
				f5.write(w[0])
				f5.close()
				os.system("fst-parse ../src/telugu_multiple.a ../src/multiplelex > ../src/out")
				f5=open("../src/out","r")
				for j in f5:
					if j.find('analysis')!=-1:
						nouns[w[0]]=w[0]
						b.append(a[i])
					else:
						j=j.split('<')[0]
						nouns[w[0]]=j
						b.append(j+'_'+w[1])
					break
				f5.close()
		b=line[:2]+b+[line[-1]]
		b=' '.join(b)
	#	print b
		f2.write(b+'\n')


#--------------------------------------------------------------------------------------------------------------------
f2=open("../src/telugu_morphed.txt","r")
f3=open("../src/telugu_test_morphed.txt","r")
f4=open("../src/telugu_morphed.out","w")



#------------------------------ TRANSMISSION AND EMISSION MATRIX -----------------------------------------------------
count=0
for line in f2:
	line=line.replace('\n','')
	count+=1
	if line!='':
		line=line.split(' ')[2:-1]
		old='start'
		for i in range(len(line)):
			w=line[i].split('_')
			if len(w)==2:
				tagset[w[1]]+=1
				unigrams+=1
				if old!='':
					transmission[old][w[1]]+=1
				try:
					emission[w[0]][w[1]]+=1
				except:
					emission[w[0]]=tags.copy()
					emission[w[0]][w[1]]=1
				old=w[1]
		try:
			transmission[old]['stop']+=1
		except:
			transmission[old]['stop']=1


#----------------------------------------------------------------------------------------------------------
######## NO OF SENTENSES TRAINING
tagset['start']=count

#---------------------------------- USELESS TAGS DELETING ---------------------------------------------------
for i in tagset.keys():
	if tagset[i]==0:
		del tags[i]


#---------------------------------- EMISSION PROBABILITIES -------------------------------------------------
for i in emission.keys():
	#	count=0
	#for j in tags.keys():
	#	count=count+emission[i][j]
	for j in tags.keys():
		if tagset[j]!=0:		
			emission[i][j]=emission[i][j]*1.0/tagset[j]

#---------------------------------- TRANSMISSION PROBABILITIES -------------------------------------------------
for i in transmission.keys():
	for j in tags.keys():
		if  tagset[i]!=0:
			transmission[i][j]=transmission[i][j]*1.0/tagset[i]
	try:
		transmission[i]['stop']=transmission[i]['stop']*1.0/tagset['start']
	except:
		transmission[i]['stop']=0



#------------------------------------- VITERBI ALGORITHM ----------------------------------------------------
def viterbi(line):
	global transmission
	global emission,tags,tagset
	a=line.replace('\n','')
	a=a.split(' ')[2:-1]
	vb=[]
	for i in range(len(a)):
		vb.append({})
		for j in tags.keys():
			vb[i][j]=[1,[]]
	m=-1.0
	fmax='NN'
	temp=None
	for k in range(len(a)):
		#print a[k],k
		for v in tags.keys():
			m=-1
			val=0
			if k==0:
				#vb[k][v][0]=(transmission['start'][v])*(emission[a[k]][v])
				try:
					vb[k][v][0]=(emission[a[k]][v])
				except:
					vb[k][v][0]=1.0/(tagset[v]+len(tagset))
				try:
					vb[k][v][0]*=transmission['start'][v]
				except:
					vb[k][v][0]*=1.0/(tagset['start']+len(tagset))
				vb[k][v][1].append(v)
			else:
				for u in tags.keys():
					val=vb[k-1][u][0]
					try:
						val*=(emission[a[k]][v])
					except:
						val*=1.0/(tagset[v]+len(tagset))
					try:
						if transmission[u][v]:
							val*=transmission[u][v]
						else:
							val*=1.0/(unigrams*1000)
					except:
						val*=1.0/(tagset[u]+len(tagset))
					if val>=m:
						m=val
						fmax=u
				#	if k==5 and len(a)>4 and a[3]=='hEkteyara' and u=='PSP':
				#		print vb[k-1][u][1] ,val , u , v, a[k] , emission[a[k]][v] , transmission[u][v] 
				vb[k][v][0]=m
				m=-1
				tagmax=''
				for u in tags.keys():
					val=vb[k][v][0]*vb[k-1][u][0]
					if val>=m:
						m=val
						tagmax=u
				vb[k][v][1]=vb[k-1][tagmax][1][:]
				vb[k][v][1].append(v)
			#	if len(a)>4 and a[3]=='hEkteyara':
			#		print vb[k-1][tagmax][1] , vb[k][v][1], tagmax , a[k] , v , vb[k][v][0] 
	m=-1
	length=len(a)
	ans=None
	for i in vb[length-1]:
		if vb[length-1][i][0]>m:
			m=vb[length-1][i][0]
			ans=vb[length-1][i][1]

#	print ans
	return ans


#------------------------------------ TESTING INPUT  --------------------------------------

count=0

for line in f3:
	count+=1
	#ans=viterbi("hin_0001 \" Apake hinxI pasanxa karane para KuSI huI \"")
	ans=viterbi(line)
	ans=['','']+ans+['']
	a=line.replace('\n','') 
	a=a.split(' ')
	sentence=''
	cnt=0
	for i,j in zip(a,ans):
		cnt+=1
		if cnt!=1 and cnt!=2 and cnt!=len(a):
			sentence+=i+'_'+j+' '
		else:
			sentence+=i+j+' '
	f4.write(sentence+'\n')
	print sentence

os.system("rm ../src/telugu_test_morphed.txt ../src/telugu_morphed.txt ../src/multiplelex ../src/out")

'''
print len(emission),len(transmission)
print tagset
print unigrams
'''
