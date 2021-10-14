"""
Code made by Francisco Garcia Araya garcicia@gmail.com

this code was written for a specific scientific research, and its reproduction for commercial use is forbidden

IMPORTANT!!!!

read and complete the configuration parameters before use
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
from scipy.stats import mannwhitneyu


def isNaN(num):
    if float('-inf') < float(num) < float('inf'):
        return 0
    else:
        return 1
"""
  __
 /    \
| STOP |
 \ __ /
   ||
   ||
   ||
   ||
   ||
 ~~~~~~~

if the code is not working apropiately comente the next line
"""
np.warnings.filterwarnings('ignore')



"""
names of files and list of names
"""
print("The whale means a successful execution of this code")
print("don't worry about warnings or other messages that code can give you")
print(" ")

boats= ('13C_coast.boat','18O_ocean.boat',  'dd_coast.boat', '13C_ocean.boat', 'dd_ocean.boat', '18O_coast.boat') # names of files with isotopic values
boatsT= ('13C Coast','18O Ocean',  'dd Coast', '13C Ocean', 'dd Ocean', '18O Coast') #names for the titles writting
c_o=(1,0,1,0,0,1) #configuration if is acoastal or oceanic value
sal_isotopic_x=([32.5,36.],[32.5,36.] , [32.5,36.], [32.5,36.],[32.5,36.],  [32.5,36.])
sal_isotopic_y=([-1.6,2.5], [-1.,1.5], [-4.,4.], [-1.6,2.5],[-4.,4.],   [-1.,1.5])


c_data=np.loadtxt('coast_data.boat', dtype=str)
o_data=np.loadtxt('ocean_data.boat', dtype=str)
c_data_M=np.loadtxt('coast_data.boat', dtype=float,skiprows=1)
o_data_M=np.loadtxt('ocean_data.boat', dtype=float,skiprows=1)
c_data_M=c_data_M.T
o_data_M=o_data_M.T

"""
Values of plot parameter
"""

v_mins=(-1,            -1,        -4,        -1,        -4,               -1) #list of values to use in the isotopic histograms
v_maxs=(2.3,            1,        3,        2.3,        3,                1) #list of values to use in the isotopic histograms

Nbins_ESSW=20
Nbins_AAIW=20
Nbins_PDW=20
Nbins_STW=20
Nbins_SAAW=20
lw_broad=4
lw_narrow=2
scatter_fontsize=15
histograms_fontsize =20
p_limit = 0.05
number_data = 3  # recomend at least 3, is minimun data in a list for the code to create histograms ans thoer graps
percent_value = 49.99999999 # minimum percent of a certain water mass 
size_font = 25
size_font_sal = 25
number_decimal = '.2f'

range_temp   = [0,25]
range_sal    = [32.5,36]
range_oxigen = [0,400]
range_PO4    = [0,3.5]
range_NO2    = [0,9]
range_NO3    = [0,50]
range_SiO4   = [0,130]
range_13C_corrected=[-1.6 , 2.5]
marker_ocean= 'D'  
marker_coast= 'o'
marker_raw= 'x'


"""
triggers to select the parts of the code that actually going to run
# positive in ('s','S','y','Y','O','o',1)
"""

print("possitive answers are ", 's','S','y','Y','O','o',1)

manual= input("Do you want to manually select what to do? y/n  ")



if manual in ('s','S','y','Y','O','o',1):
	chemical_histograms=input('Do you want to make the chemical histograms?  y/n  ')
	isotopic_histograms=input('Do you want to make the isotopic histograms?  y/n  ')
	matt_w=input('Do you want to make the Mann Whitney analysis?  y/n  ')
	corr_13C=input('Do you want to calculate 13Csea-air exange?')
	if corr_13C in ('s','S','y','Y','O','o',1):
		o_13C_as_O=1
		c_13C_as_O=1
		o_13C_as_PO4=1
		c_13C_as_PO4=1
		corrected_13C_histograms=1
	else:
		o_13C_as_O=0
		c_13C_as_O=0
		o_13C_as_PO4=0
		c_13C_as_PO4=0
		corrected_13C_histograms=0
		

	plot_salinity_o =input('Do you want to make the linear regression for isotopic values vs salinity in the oceanic sectios? y/n  ')
	plot_salinity_c =input('Do you want to make the linear regression for isotopic values vs salinity in the coastal section? y/n  ')
else:
	chemical_histograms = 1
	isotopic_histograms = 1
	
	o_13C_as_O=1
	c_13C_as_O=1
	o_13C_as_PO4=1
	c_13C_as_PO4=1
	corrected_13C_histograms=1

	matt_w = 1

	plot_salinity_o = 1
	plot_salinity_c = 1





for j in range(len(boats)):



	DATA = np.loadtxt(boats[j], dtype=str)
	DATA_M = np.loadtxt(boats[j], dtype=float, skiprows=1) 
	DATA_M = DATA_M.T

	DATA_M2=DATA_M
	o_data_M2=o_data_M
	c_data_M2=c_data_M


	ESSW=[[],[],[],[]]
	AAIW=[[],[],[],[]]
	PDW =[[],[],[],[]]
	STW =[[],[],[],[]]
	SAAW=[[],[],[],[]]

	ESSW_salinity=[]
	AAIW_salinity=[]
	PDW_salinity=[]
	STW_salinity=[]
	SAAW_salinity=[]

	S_limit= -10.
	N_limit= -54.
	L_limit=4100.
	U_limit=49.


	for k in range(len(DATA_M[0])):

		if DATA_M[3][k] > percent_value:
			if DATA_M[1][k] > U_limit and DATA_M[1][k] < L_limit:
				if DATA_M[0][k] < S_limit and DATA_M[0][k]> N_limit:
					if isNaN(DATA_M[2][k]) == 0:
						ESSW[0].append(DATA_M[0][k])
						ESSW[1].append(DATA_M[1][k]*(-1.))
						ESSW[2].append(DATA_M[2][k])
						ESSW[3].append(DATA_M[3][k])
						if c_o[j]== 1:
							ESSW_salinity.append(c_data_M2[6][k])
						else:
							ESSW_salinity.append(o_data_M2[6][k])
						
										
		
		if DATA_M[4][k] > percent_value:
			if DATA_M[1][k] > U_limit and DATA_M[1][k] < L_limit:
				if DATA_M[0][k] < S_limit and DATA_M[0][k]> N_limit:
					if isNaN(DATA_M[2][k]) == 0:
						AAIW[0].append(DATA_M[0][k])
						AAIW[1].append(DATA_M[1][k]*(-1.))
						AAIW[2].append(DATA_M[2][k])
						AAIW[3].append(DATA_M[4][k])
						if c_o[j]== 1:
							AAIW_salinity.append(c_data_M2[6][k])
						else:
							AAIW_salinity.append(o_data_M2[6][k])
						


		if DATA_M[5][k] > percent_value:
			if DATA_M[1][k] > U_limit and DATA_M[1][k] < L_limit:
				if DATA_M[0][k] < S_limit and DATA_M[0][k]> N_limit:
					if isNaN(DATA_M[2][k]) == 0:
						PDW[0].append(DATA_M[0][k])
						PDW[1].append(DATA_M[1][k]*(-1.))
						PDW[2].append(DATA_M[2][k])
						PDW[3].append(DATA_M[5][k])
						if c_o[j]== 1:
							PDW_salinity.append(c_data_M2[6][k])
						else:
							PDW_salinity.append(o_data_M2[6][k])						
				
		if DATA_M[6][k] > percent_value:
			if DATA_M[1][k] > U_limit and DATA_M[1][k] < L_limit:
				if DATA_M[0][k] < S_limit and DATA_M[0][k]> N_limit:
					if isNaN(DATA_M[2][k]) == 0:
						STW[0].append(DATA_M[0][k])
						STW[1].append(DATA_M[1][k]*(-1.))
						STW[2].append(DATA_M[2][k])
						STW[3].append(DATA_M[6][k])
						if c_o[j]== 1:
							STW_salinity.append(c_data_M2[6][k])
						else:
							STW_salinity.append(o_data_M2[6][k])						

		if DATA_M[7][k] > percent_value:
			if DATA_M[1][k] > U_limit and DATA_M[1][k] < L_limit:
				if DATA_M[0][k] < S_limit and DATA_M[0][k]> N_limit:
					if isNaN(DATA_M[2][k]) == 0:
						SAAW[0].append(DATA_M[0][k])
						SAAW[1].append(DATA_M[1][k]*(-1.))
						SAAW[2].append(DATA_M[2][k])
						SAAW[3].append(DATA_M[7][k])
						if c_o[j]== 1:
							SAAW_salinity.append(c_data_M2[6][k])
						else:
							SAAW_salinity.append(o_data_M2[6][k])





	mtt_list  = [ESSW[2], AAIW[2],PDW[2],STW[2],SAAW[2]]
	mtt_names = ('ESSW','AAIW','PDW','STW','SAAW')



	if matt_w in  ('s','S','y','Y','O','o',1):
		print("Mann Whitney statistical values")
		for jj in range(len(mtt_list)):
			for kk in range(len(mtt_list)):
				if mtt_list[jj] != mtt_list[kk]:


					results = mannwhitneyu(mtt_list[jj] , mtt_list[kk] )
					print(boatsT[j], mtt_names[jj],len(mtt_list[jj]), mtt_names[kk],len(mtt_list[kk]), "p value = " ,format(results[1],number_decimal) )
			
	if plot_salinity_c in ('s','S','y','Y','O','o',1):
		if c_o[j] == 1:
			print("Linear regression statistical values")
			plt.title('Salinity vs isotopic value for  '+str(boatsT[j]))

			plt.scatter(c_data_M2[6],DATA_M2[2], c='k', zorder=1, s=10, marker= marker_raw,label='Raw data')


			if len(ESSW[2]) > number_data:
				plt.scatter(ESSW_salinity, ESSW[2], c='m', zorder=2, edgecolor='k', s=40, label='ESSW')
				
				a_ESSW, b_ESSW, r_ESSW, p_ESSW, str_ESSW  = linregress(ESSW_salinity, ESSW[2])
				print(boatsT[j],'ESSW','a',format(a_ESSW, number_decimal), 'c',format(b_ESSW,number_decimal), 'r',format(r_ESSW,number_decimal), 'r2',format(r_ESSW**2,number_decimal), 'p',format(p_ESSW, number_decimal), 'str',format(str_ESSW,number_decimal))

				if p_ESSW <= p_limit:

					XX_ESSW = np.linspace(np.nanmin(ESSW_salinity),np.nanmax(ESSW_salinity),5)

					YY_ESSW = (XX_ESSW*a_ESSW)+b_ESSW

					plt.plot(XX_ESSW,YY_ESSW, ls='-', marker='None',zorder=7,lw=lw_broad, c='k')
					plt.plot(XX_ESSW,YY_ESSW, ls='-', marker='None',zorder=8,lw=lw_narrow, c='m')



			if len(AAIW[2]) > number_data:
				plt.scatter(AAIW_salinity, AAIW[2], c='lime', zorder=3, edgecolor='k', s=40, label='AAIW')

				a_AAIW, b_AAIW, r_AAIW, p_AAIW, str_AAIW  = linregress(AAIW_salinity, AAIW[2])
				print(boatsT[j],'AAIW','a',format(a_AAIW, number_decimal), 'c',format(b_AAIW,number_decimal), 'r',format(r_AAIW,number_decimal), 'r2',format(r_AAIW**2,number_decimal), 'p',format(p_AAIW, number_decimal), 'str',format(str_AAIW,number_decimal))
				if p_AAIW <= p_limit:
					XX_AAIW = np.linspace(np.nanmin(AAIW_salinity),np.nanmax(AAIW_salinity),5)

					YY_AAIW = (XX_AAIW*a_AAIW)+b_AAIW

					plt.plot(XX_AAIW,YY_AAIW, ls='-', marker='None',zorder=9,lw=lw_broad, c='k')
					plt.plot(XX_AAIW,YY_AAIW, ls='-', marker='None',zorder=10,lw=lw_narrow, c='lime')

			if len(PDW[2]) > number_data:
				plt.scatter(PDW_salinity, PDW[2], c='r', zorder=4, edgecolor='k', s=40, label='PDW')

				a_PDW, b_PDW, r_PDW, p_PDW, str_PDW  = linregress(PDW_salinity, PDW[2])
				print(boatsT[j],'PDW','a',format(a_PDW, number_decimal), 'c',format(b_PDW,number_decimal), 'r',format(r_PDW,number_decimal), 'r2',format(r_PDW**2,number_decimal), 'p',format(p_PDW, number_decimal), 'str',format(str_PDW,number_decimal))			

				if p_PDW <= p_limit:
					XX_PDW = np.linspace(np.nanmin(PDW_salinity),np.nanmax(PDW_salinity),5)

					YY_PDW = (XX_PDW*a_PDW)+b_PDW

					plt.plot(XX_PDW,YY_PDW, ls='-', marker='None',zorder=11,lw=lw_broad, c='k')
					plt.plot(XX_PDW,YY_PDW, ls='-', marker='None',zorder=12,lw=lw_narrow , c='r')

			if len(STW[2]) > number_data:
				plt.scatter(STW_salinity, STW[2], c='c', zorder=5, edgecolor='k', s=40, label='STW')

				a_STW, b_STW, r_STW, p_STW, str_STW  = linregress(STW_salinity, STW[2])
				print(boatsT[j],'STW','a',format(a_STW, number_decimal), 'c',format(b_STW,number_decimal), 'r',format(r_STW,number_decimal), 'r2',format(r_STW**2,number_decimal), 'p',format(p_STW, number_decimal), 'str',format(str_STW,number_decimal))
				if p_STW <= p_limit:
					XX_STW = np.linspace(np.nanmin(STW_salinity),np.nanmax(STW_salinity),5)

					YY_STW = (XX_STW*a_STW)+b_STW

					plt.plot(XX_STW,YY_STW, ls='-', marker='None',zorder=13,lw=lw_broad, c='k')
					plt.plot(XX_STW,YY_STW, ls='-', marker='None',zorder=14,lw=lw_narrow, c='c')

			if len(SAAW[2]) > number_data:
				plt.scatter(SAAW_salinity, SAAW[2], c='y', zorder=6, edgecolor='k', s=40, label='SAAW')		

				a_SAAW, b_SAAW, r_SAAW, p_SAAW, str_SAAW  = linregress(SAAW_salinity, SAAW[2])
				print(boatsT[j],'SAAW','a',format(a_SAAW, number_decimal), 'c',format(b_SAAW,number_decimal), 'r',format(r_SAAW,number_decimal), 'r2',format(r_SAAW**2,number_decimal), 'p',format(p_SAAW, number_decimal), 'str',format(str_SAAW,number_decimal))			
				
				if p_SAAW <= p_limit:

					XX_SAAW = np.linspace(np.nanmin(SAAW_salinity),np.nanmax(SAAW_salinity),5)

					YY_SAAW = (XX_SAAW*a_SAAW)+b_SAAW

					plt.plot(XX_SAAW,YY_SAAW, ls='-', marker='None',zorder=15,lw=lw_broad, c='k')
					plt.plot(XX_SAAW,YY_SAAW, ls='-', marker='None',zorder=16,lw=lw_narrow, c='y')
			plt.yticks(fontsize= scatter_fontsize)
			plt.xticks(fontsize= scatter_fontsize)
			plt.legend(fontsize=12, markerscale=int(2))
			plt.xlim(sal_isotopic_x[j])
			plt.ylim(sal_isotopic_y[j])
			plt.savefig(str(boatsT[j])+"Coastal_salinity_ratios.svg",  format='svg', dpi=300)
			plt.close()

	if plot_salinity_o in ('s','S','y','Y','O','o',1):
		if c_o[j] == 0 :
			print("Linear regression statistical values")
			plt.title('Salinity vs isotopic value for  '+str(boatsT[j]))

			plt.scatter(o_data_M2[6],DATA_M2[2], c='k', zorder=1, s=10, marker= marker_raw,label='Raw data')




			if len(ESSW[2]) > number_data:
				plt.scatter(ESSW_salinity, ESSW[2],marker= marker_ocean, c='m', zorder=2, edgecolor='k', s=40, label='ESSW')
				
				a_ESSW, b_ESSW, r_ESSW, p_ESSW, str_ESSW  = linregress(ESSW_salinity, ESSW[2])
				print(boatsT[j],'ESSW','a',format(a_ESSW, number_decimal), 'c',format(b_ESSW,number_decimal), 'r',format(r_ESSW,number_decimal), 'r2',format(r_ESSW**2,number_decimal), 'p',format(p_ESSW, number_decimal), 'str',format(str_ESSW,number_decimal))

				if p_ESSW <= p_limit:

					XX_ESSW = np.linspace(np.nanmin(ESSW_salinity),np.nanmax(ESSW_salinity),5)

					YY_ESSW = (XX_ESSW*a_ESSW)+b_ESSW

					plt.plot(XX_ESSW,YY_ESSW, ls='-', marker='None',zorder=7,lw=lw_broad, c='k')
					plt.plot(XX_ESSW,YY_ESSW, ls='-', marker='None',zorder=8,lw=lw_narrow, c='m')



			if len(AAIW[2]) > number_data:
				plt.scatter(AAIW_salinity, AAIW[2],marker= marker_ocean, c='lime', zorder=3, edgecolor='k', s=40, label='AAIW')

				a_AAIW, b_AAIW, r_AAIW, p_AAIW, str_AAIW  = linregress(AAIW_salinity, AAIW[2])
				print(boatsT[j],'AAIW','a',format(a_AAIW, number_decimal), 'c',format(b_AAIW,number_decimal), 'r',format(r_AAIW,number_decimal), 'r2',format(r_AAIW**2,number_decimal), 'p',format(p_AAIW, number_decimal), 'str',format(str_AAIW,number_decimal))
				if p_AAIW <= p_limit:
					XX_AAIW = np.linspace(np.nanmin(AAIW_salinity),np.nanmax(AAIW_salinity),5)

					YY_AAIW = (XX_AAIW*a_AAIW)+b_AAIW

					plt.plot(XX_AAIW,YY_AAIW, ls='-', marker='None',zorder=9,lw=lw_broad, c='k')
					plt.plot(XX_AAIW,YY_AAIW, ls='-', marker='None',zorder=10,lw=lw_narrow, c='lime')

			if len(PDW[2]) > number_data:
				plt.scatter(PDW_salinity, PDW[2],marker= marker_ocean, c='r', zorder=4, edgecolor='k', s=40, label='PDW')

				a_PDW, b_PDW, r_PDW, p_PDW, str_PDW  = linregress(PDW_salinity, PDW[2])
				print(boatsT[j],'PDW','a',format(a_PDW, number_decimal), 'c',format(b_PDW,number_decimal), 'r',format(r_PDW,number_decimal), 'r2',format(r_PDW**2,number_decimal), 'p',format(p_PDW, number_decimal), 'str',format(str_PDW,number_decimal))			

				if p_PDW <= p_limit:
					XX_PDW = np.linspace(np.nanmin(PDW_salinity),np.nanmax(PDW_salinity),5)

					YY_PDW = (XX_PDW*a_PDW)+b_PDW

					plt.plot(XX_PDW,YY_PDW, ls='-', marker='None',zorder=11,lw=lw_broad, c='k')
					plt.plot(XX_PDW,YY_PDW, ls='-', marker='None',zorder=12,lw=lw_narrow , c='r')

			if len(STW[2]) > number_data:
				plt.scatter(STW_salinity, STW[2],marker= marker_ocean, c='c', zorder=5, edgecolor='k', s=40, label='STW')

				a_STW, b_STW, r_STW, p_STW, str_STW  = linregress(STW_salinity, STW[2])
				print(boatsT[j],'STW','a',format(a_STW, number_decimal), 'c',format(b_STW,number_decimal), 'r',format(r_STW,number_decimal), 'r2',format(r_STW**2,number_decimal), 'p',format(p_STW, number_decimal), 'str',format(str_STW,number_decimal))
				if p_STW <= p_limit:
					XX_STW = np.linspace(np.nanmin(STW_salinity),np.nanmax(STW_salinity),5)

					YY_STW = (XX_STW*a_STW)+b_STW

					plt.plot(XX_STW,YY_STW, ls='-', marker='None',zorder=13,lw=lw_broad, c='k')
					plt.plot(XX_STW,YY_STW, ls='-', marker='None',zorder=14,lw=lw_narrow, c='c')

			if len(SAAW[2]) > number_data:
				plt.scatter(SAAW_salinity, SAAW[2],marker= marker_ocean, c='y', zorder=6, edgecolor='k', s=40, label='SAAW')		

				a_SAAW, b_SAAW, r_SAAW, p_SAAW, str_SAAW  = linregress(SAAW_salinity, SAAW[2])
				print(boatsT[j],'SAAW','a',format(a_SAAW, number_decimal), 'c',format(b_SAAW,number_decimal), 'r',format(r_SAAW,number_decimal), 'r2',format(r_SAAW**2,number_decimal), 'p',format(p_SAAW, number_decimal), 'str',format(str_SAAW,number_decimal))			
				
				if p_SAAW <= p_limit:

					XX_SAAW = np.linspace(np.nanmin(SAAW_salinity),np.nanmax(SAAW_salinity),5)

					YY_SAAW = (XX_SAAW*a_SAAW)+b_SAAW

					plt.plot(XX_SAAW,YY_SAAW, ls='-', marker='None',zorder=15,lw=lw_broad, c='k')
					plt.plot(XX_SAAW,YY_SAAW, ls='-', marker='None',zorder=16,lw=lw_narrow, c='y')
			plt.yticks(fontsize=scatter_fontsize)
			plt.xticks(fontsize=scatter_fontsize)
			plt.legend(fontsize=12, markerscale=int(2))
			plt.xlim(sal_isotopic_x[j])
			plt.ylim(sal_isotopic_y[j])
			plt.savefig(str(boatsT[j])+"Oceanic_salinity_ratios.svg",  format='svg', dpi=300)
			plt.close()
			#plt.show()

	if isotopic_histograms in ('s','S','y','Y','O','o',1):		
		if len(ESSW[2]) > number_data:
			plt.xlim([v_mins[j] , v_maxs[j]])
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			plt.hist(ESSW[2],  facecolor="r", edgecolor="k")
			plt.title(str(boats[j])+"ESSW"+str(len(ESSW[2]))+"points \n Mean = "+str(np.nanmean(ESSW[2]))+"\n std = "+str(np.nanstd(ESSW[2])))
			plt.savefig(str(boatsT[j])+"ESSW.svg",  format='svg', dpi=300)
			plt.close()
			
		else:
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			plt.title(str(boats[j])+"ESSW"+str(len(ESSW[2]))+"points")
			plt.savefig(str(boatsT[j])+"ESSW.svg",  format='svg', dpi=300)
			plt.close()

		if len(AAIW[2]) > number_data:
			
			plt.xlim([v_mins[j] , v_maxs[j]])
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			
			plt.hist(AAIW[2],  facecolor="r", edgecolor="k", range=(v_mins[j] , v_maxs[j]))
			plt.title(str(boats[j])+"AAIW"+str(len(AAIW[2]))+"points \n Mean = "+str(np.nanmean(AAIW[2]))+"\n std = "+str(np.nanstd(AAIW[2])))
			plt.savefig(str(boatsT[j])+"AAIW.svg",  format='svg', dpi=300)
			
			plt.close()
		else:
			
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			plt.title(str(boats[j])+"AAIW"+str(len(AAIW[2]))+"points")
			plt.savefig(str(boatsT[j])+"AAIW.svg",  format='svg', dpi=300)
			
			plt.close()
		if len(PDW[2]) > number_data:
			
			plt.xlim([v_mins[j] , v_maxs[j]])
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			
			plt.hist(PDW[2],  facecolor="r", edgecolor="k", range=(v_mins[j] , v_maxs[j]))
			plt.title(str(boats[j])+"PDW"+str(len(PDW[2]))+"points \n Mean = "+str(np.nanmean(PDW[2]))+"\n std = "+str(np.nanstd(PDW[2])))
			plt.savefig(str(boatsT[j])+"PDW.svg",  format='svg', dpi=300)
			
			plt.close()
		else:
			
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)			
			plt.title(str(boats[j])+"PDW"+str(len(PDW[2]))+"points")
			plt.savefig(str(boatsT[j])+"PDW.svg",  format='svg', dpi=300)
			
			plt.close()		
		if len(STW[2]) > number_data:
			
			plt.xlim([v_mins[j] , v_maxs[j]])
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			
			plt.hist(STW[2], facecolor="r", edgecolor="k", range=(v_mins[j] , v_maxs[j]))
			plt.title(str(boats[j])+"STW"+str(len(STW[2]))+"points \n Mean = "+str(np.nanmean(STW[2]))+"\n std = "+str(np.nanstd(STW[2])))
			plt.savefig(str(boatsT[j])+"STW.svg",  format='svg', dpi=300)
			
			plt.close()
		else:
			
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			plt.title(str(boats[j])+"STW"+str(len(STW[2]))+"points")
			plt.savefig(str(boatsT[j])+"STW.svg",  format='svg', dpi=300)
			
			plt.close()	

		if len(SAAW[2]) > number_data:
			plt.xlim([v_mins[j] , v_maxs[j]])
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			
			plt.hist(SAAW[2], facecolor="r", edgecolor="k", range=(v_mins[j] , v_maxs[j]))
			plt.title(str(boats[j])+"SAAW"+str(len(SAAW[2]))+"points \n Mean = "+str(np.nanmean(SAAW[2]))+"\n std = "+str(np.nanstd(SAAW[2])))
			plt.savefig(str(boatsT[j])+"SAAW.svg",  format='svg', dpi=300)
			
			plt.close()
		else:
			
			plt.yticks(fontsize= histograms_fontsize)
			plt.xticks(fontsize= histograms_fontsize)
			plt.title(str(boats[j])+"SAAW"+str(len(SAAW[2]))+"points")
			plt.savefig(str(boatsT[j])+"SAAW.svg",  format='svg', dpi=300)
			
			plt.close()

if chemical_histograms in ('s','S','y','Y','O','o',1):

	c_ESSW_salinity=[]
	c_AAIW_salinity=[]
	c_PDW_salinity=[]
	c_STW_salinity=[]
	c_SAAW_salinity=[]

	c_ESSW_NO2   =[]
	c_AAIW_NO2   =[]
	c_PDW_NO2   =[]
	c_STW_NO2   =[]
	c_SAAW_NO2   =[]

	c_ESSW_NO3   =[]
	c_AAIW_NO3   =[]
	c_PDW_NO3   =[]
	c_STW_NO3   =[]
	c_SAAW_NO3   =[]

	c_ESSW_O   =[]
	c_AAIW_O   =[]
	c_PDW_O   =[]
	c_STW_O   =[]
	c_SAAW_O   =[]

	c_ESSW_PO4   =[]
	c_AAIW_PO4   =[]
	c_PDW_PO4   =[]
	c_STW_PO4   =[]
	c_SAAW_PO4   =[]

	c_ESSW_SiO4   =[]
	c_AAIW_SiO4   =[]
	c_PDW_SiO4   =[]
	c_STW_SiO4   =[]
	c_SAAW_SiO4   =[]

	c_ESSW_temp   =[]
	c_AAIW_temp   =[]
	c_PDW_temp   =[]
	c_STW_temp   =[]
	c_SAAW_temp   =[]	

	for k in range(len(c_data_M2[0])):
		if c_data_M2[10][k] > percent_value:

			c_ESSW_NO2.append(c_data_M2[2][k])
			c_ESSW_NO3.append(c_data_M2[3][k])
			c_ESSW_O.append(c_data_M2[4][k])
			c_ESSW_PO4.append(c_data_M2[5][k])
			c_ESSW_salinity.append(c_data_M2[6][k])
			c_ESSW_SiO4.append(c_data_M2[7][k])
			c_ESSW_temp.append(c_data_M2[8][k])
		if c_data_M2[11][k] > percent_value:

			c_AAIW_NO2.append(c_data_M2[2][k])
			c_AAIW_NO3.append(c_data_M2[3][k])
			c_AAIW_O.append(c_data_M2[4][k])
			c_AAIW_PO4.append(c_data_M2[5][k])
			c_AAIW_salinity.append(c_data_M2[6][k])
			c_AAIW_SiO4.append(c_data_M2[7][k])
			c_AAIW_temp.append(c_data_M2[8][k])

		if c_data_M2[12][k] > percent_value:
			c_PDW_NO2.append(c_data_M2[2][k])
			c_PDW_NO3.append(c_data_M2[3][k])
			c_PDW_O.append(c_data_M2[4][k])
			c_PDW_PO4.append(c_data_M2[5][k])
			c_PDW_salinity.append(c_data_M2[6][k])
			c_PDW_SiO4.append(c_data_M2[7][k])
			c_PDW_temp.append(c_data_M2[8][k])

		if c_data_M2[13][k] > percent_value:
			c_STW_NO2.append(c_data_M2[2][k])
			c_STW_NO3.append(c_data_M2[3][k])
			c_STW_O.append(c_data_M2[4][k])
			c_STW_PO4.append(c_data_M2[5][k])
			c_STW_salinity.append(c_data_M2[6][k])
			c_STW_SiO4.append(c_data_M2[7][k])
			c_STW_temp.append(c_data_M2[8][k])
		if c_data_M2[14][k] > percent_value:

			c_SAAW_NO2.append(c_data_M2[2][k])
			c_SAAW_NO3.append(c_data_M2[3][k])
			c_SAAW_O.append(c_data_M2[4][k])
			c_SAAW_PO4.append(c_data_M2[5][k])
			c_SAAW_salinity.append(c_data_M2[6][k])
			c_SAAW_SiO4.append(c_data_M2[7][k])
			c_SAAW_temp.append(c_data_M2[8][k])
		


	if len(c_ESSW_NO2 ) > number_data:
		
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_ESSW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_ESSW NO2"+str(len(c_ESSW_NO2))+"points \n Mean = "+str(format((np.nanmean(c_ESSW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(c_ESSW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_ESSW_NO2.svg",  format='svg', dpi=300)
		
		plt.close()
	if len(c_ESSW_NO3 ) > number_data:
		
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_ESSW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_ESSW NO3"+str(len(c_ESSW_NO3))+"points \n Mean = "+str(format((np.nanmean(c_ESSW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(c_ESSW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		
		plt.savefig("coast_c_ESSW_NO3.svg",  format='svg', dpi=300)
		
		plt.close()
	if len(c_ESSW_O ) > number_data:
		
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_ESSW_O ,  facecolor="r", edgecolor="k")
		plt.title("coast c_ESSW O "+str(len(c_ESSW_O))+"points \n Mean = "+str(format((np.nanmean(c_ESSW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(c_ESSW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		
		plt.savefig("coast_c_ESSW_O.svg",  format='svg', dpi=300)
		
		plt.close()
	if len(c_ESSW_PO4 ) > number_data:
		
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_ESSW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_ESSW PO4 "+str(len(c_ESSW_PO4))+"points \n Mean = "+str(format((np.nanmean(c_ESSW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_ESSW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		
		plt.savefig("coast_c_ESSW_PO4.svg",  format='svg', dpi=300)
		
		plt.close()
	if len(c_ESSW_SiO4 ) > number_data:
		
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_ESSW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_ESSW SiO4 "+str(len(c_ESSW_SiO4))+"points \n Mean = "+str(format((np.nanmean(c_ESSW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_ESSW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		
		plt.savefig("coast_c_ESSW_SiO4.svg",  format='svg', dpi=300)
		
		plt.close()
	if len(c_ESSW_temp ) > number_data:
		
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_ESSW_temp ,  facecolor="r", edgecolor="k")
		plt.title("coast c_ESSW temp "+str(len(c_ESSW_temp))+"points \n Mean = "+str(format((np.nanmean(c_ESSW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(c_ESSW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		
		plt.savefig("coast_c_ESSW_temp.svg",  format='svg', dpi=300)
		
		plt.close()
	if len(c_ESSW_salinity ) > number_data:
		
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_ESSW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("coast c_ESSW salinity "+str(len(c_ESSW_salinity))+"points \n Mean = "+str(format((np.nanmean(c_ESSW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(c_ESSW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		
		plt.savefig("coast_c_ESSW_salinity.svg",  format='svg', dpi=300)
		
		plt.close()

	if len(c_AAIW_NO2 ) > number_data:

		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_AAIW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_AAIW NO2"+str(len(c_AAIW_NO2))+"points \n Mean = "+str(format((np.nanmean(c_AAIW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(c_AAIW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_AAIW_NO2.svg",  format='svg', dpi=300)

		plt.close()
	if len(c_AAIW_NO3 ) > number_data:

		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_AAIW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_AAIW NO3"+str(len(c_AAIW_NO3))+"points \n Mean = "+str(format((np.nanmean(c_AAIW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(c_AAIW_NO3)),number_decimal)),  fontsize=histograms_fontsize)

		plt.savefig("coast_c_AAIW_NO3.svg",  format='svg', dpi=300)

		plt.close()
	if len(c_AAIW_O ) > number_data:

		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_AAIW_O ,  facecolor="r", edgecolor="k")
		plt.title("coast c_AAIW O "+str(len(c_AAIW_O))+"points \n Mean = "+str(format((np.nanmean(c_AAIW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(c_AAIW_O)),number_decimal)) ,  fontsize=histograms_fontsize)

		plt.savefig("coast_c_AAIW_O.svg",  format='svg', dpi=300)

		plt.close()
	if len(c_AAIW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_AAIW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_AAIW PO4 "+str(len(c_AAIW_PO4))+"points \n Mean = "+str(format((np.nanmean(c_AAIW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_AAIW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_AAIW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_AAIW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_AAIW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_AAIW SiO4 "+str(len(c_AAIW_SiO4))+"points \n Mean = "+str(format((np.nanmean(c_AAIW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_AAIW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_AAIW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_AAIW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_AAIW_temp ,  facecolor="r", edgecolor="k")
		plt.title("coast c_AAIW temp "+str(len(c_AAIW_temp))+"points \n Mean = "+str(format((np.nanmean(c_AAIW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(c_AAIW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_AAIW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_AAIW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_AAIW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("coast c_AAIW salinity "+str(len(c_AAIW_salinity))+"points \n Mean = "+str(format((np.nanmean(c_AAIW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(c_AAIW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_AAIW_salinity.svg",  format='svg', dpi=300)
		plt.close()

	if len(c_PDW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_PDW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_PDW NO2"+str(len(c_PDW_NO2))+"points \n Mean = "+str(format((np.nanmean(c_PDW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(c_PDW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_PDW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_PDW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_PDW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_PDW NO3"+str(len(c_PDW_NO3))+"points \n Mean = "+str(format((np.nanmean(c_PDW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(c_PDW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_PDW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_PDW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_PDW_O ,  facecolor="r", edgecolor="k")
		plt.title("coast c_PDW O "+str(len(c_PDW_O))+"points \n Mean = "+str(format((np.nanmean(c_PDW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(c_PDW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("coast_c_PDW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_PDW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_PDW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_PDW PO4 "+str(len(c_PDW_PO4))+"points \n Mean = "+str(format((np.nanmean(c_PDW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_PDW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_PDW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_PDW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_PDW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_PDW SiO4 "+str(len(c_PDW_SiO4))+"points \n Mean = "+str(format((np.nanmean(c_PDW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_PDW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_PDW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_PDW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_PDW_temp ,  facecolor="r", edgecolor="k")
		plt.title("coast c_PDW temp "+str(len(c_PDW_temp))+"points \n Mean = "+str(format((np.nanmean(c_PDW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(c_PDW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_PDW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_PDW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_PDW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("coast c_PDW salinity "+str(len(c_PDW_salinity))+"points \n Mean = "+str(format((np.nanmean(c_PDW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(c_PDW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_PDW_salinity.svg",  format='svg', dpi=300)
		plt.close()

	if len(c_STW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_STW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_STW NO2"+str(len(c_STW_NO2))+"points \n Mean = "+str(format((np.nanmean(c_STW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(c_STW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_STW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_STW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_STW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_STW NO3"+str(len(c_STW_NO3))+"points \n Mean = "+str(format((np.nanmean(c_STW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(c_STW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_STW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_STW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_STW_O ,  facecolor="r", edgecolor="k")
		plt.title("coast c_STW O "+str(len(c_STW_O))+"points \n Mean = "+str(format((np.nanmean(c_STW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(c_STW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("coast_c_STW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_STW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_STW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_STW PO4 "+str(len(c_STW_PO4))+"points \n Mean = "+str(format((np.nanmean(c_STW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_STW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_STW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_STW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_STW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_STW SiO4 "+str(len(c_STW_SiO4))+"points \n Mean = "+str(format((np.nanmean(c_STW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_STW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_STW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_STW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_STW_temp ,  facecolor="r", edgecolor="k")
		plt.title("coast c_STW temp "+str(len(c_STW_temp))+"points \n Mean = "+str(format((np.nanmean(c_STW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(c_STW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_STW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_STW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_STW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("coast c_STW salinity "+str(len(c_STW_salinity))+"points \n Mean = "+str(format((np.nanmean(c_STW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(c_STW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_STW_salinity.svg",  format='svg', dpi=300)
		plt.close()


	if len(c_SAAW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_SAAW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_SAAW NO2"+str(len(c_SAAW_NO2))+"points \n Mean = "+str(format((np.nanmean(c_SAAW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(c_SAAW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_SAAW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_SAAW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_SAAW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_SAAW NO3"+str(len(c_SAAW_NO3))+"points \n Mean = "+str(format((np.nanmean(c_SAAW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(c_SAAW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_SAAW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_SAAW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_SAAW_O ,  facecolor="r", edgecolor="k")
		plt.title("coast c_SAAW O "+str(len(c_SAAW_O))+"points \n Mean = "+str(format((np.nanmean(c_SAAW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(c_SAAW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("coast_c_SAAW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_SAAW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_SAAW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_SAAW PO4 "+str(len(c_SAAW_PO4))+"points \n Mean = "+str(format((np.nanmean(c_SAAW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_SAAW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_SAAW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_SAAW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_SAAW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("coast c_SAAW SiO4 "+str(len(c_SAAW_SiO4))+"points \n Mean = "+str(format((np.nanmean(c_SAAW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(c_SAAW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("coast_c_SAAW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_SAAW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_SAAW_temp ,  facecolor="r", edgecolor="k")
		plt.title("coast c_SAAW temp "+str(len(c_SAAW_temp))+"points \n Mean = "+str(format((np.nanmean(c_SAAW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(c_SAAW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_SAAW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_SAAW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_SAAW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("coast c_SAAW salinity "+str(len(c_SAAW_salinity))+"points \n Mean = "+str(format((np.nanmean(c_SAAW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(c_SAAW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("coast_c_SAAW_salinity.svg",  format='svg', dpi=300)
		plt.close()

	o_ESSW_salinity=[]
	o_AAIW_salinity=[]
	o_PDW_salinity=[]
	o_STW_salinity=[]
	o_SAAW_salinity=[]

	o_ESSW_NO2   =[]
	o_AAIW_NO2   =[]
	o_PDW_NO2   =[]
	o_STW_NO2   =[]
	o_SAAW_NO2   =[]

	o_ESSW_NO3   =[]
	o_AAIW_NO3   =[]
	o_PDW_NO3   =[]
	o_STW_NO3   =[]
	o_SAAW_NO3   =[]

	o_ESSW_O   =[]
	o_AAIW_O   =[]
	o_PDW_O   =[]
	o_STW_O   =[]
	o_SAAW_O   =[]

	o_ESSW_PO4   =[]
	o_AAIW_PO4   =[]
	o_PDW_PO4   =[]
	o_STW_PO4   =[]
	o_SAAW_PO4   =[]

	o_ESSW_SiO4   =[]
	o_AAIW_SiO4   =[]
	o_PDW_SiO4   =[]
	o_STW_SiO4   =[]
	o_SAAW_SiO4   =[]

	o_ESSW_temp   =[]
	o_AAIW_temp   =[]
	o_PDW_temp   =[]
	o_STW_temp   =[]
	o_SAAW_temp   =[]	

	for k in range(len(o_data_M2[0])):
		if o_data_M2[10][k] > percent_value:

			o_ESSW_NO2.append(o_data_M2[2][k])
			o_ESSW_NO3.append(o_data_M2[3][k])
			o_ESSW_O.append(o_data_M2[4][k])
			o_ESSW_PO4.append(o_data_M2[5][k])
			o_ESSW_salinity.append(o_data_M2[6][k])
			o_ESSW_SiO4.append(o_data_M2[7][k])
			o_ESSW_temp.append(o_data_M2[8][k])
		if o_data_M2[11][k] > percent_value:

			o_AAIW_NO2.append(o_data_M2[2][k])
			o_AAIW_NO3.append(o_data_M2[3][k])
			o_AAIW_O.append(o_data_M2[4][k])
			o_AAIW_PO4.append(o_data_M2[5][k])
			o_AAIW_salinity.append(o_data_M2[6][k])
			o_AAIW_SiO4.append(o_data_M2[7][k])
			o_AAIW_temp.append(o_data_M2[8][k])

		if o_data_M2[12][k] > percent_value:
			o_PDW_NO2.append(o_data_M2[2][k])
			o_PDW_NO3.append(o_data_M2[3][k])
			o_PDW_O.append(o_data_M2[4][k])
			o_PDW_PO4.append(o_data_M2[5][k])
			o_PDW_salinity.append(o_data_M2[6][k])
			o_PDW_SiO4.append(o_data_M2[7][k])
			o_PDW_temp.append(o_data_M2[8][k])

		if o_data_M2[13][k] > percent_value:
			o_STW_NO2.append(o_data_M2[2][k])
			o_STW_NO3.append(o_data_M2[3][k])
			o_STW_O.append(o_data_M2[4][k])
			o_STW_PO4.append(o_data_M2[5][k])
			o_STW_salinity.append(o_data_M2[6][k])
			o_STW_SiO4.append(o_data_M2[7][k])
			o_STW_temp.append(o_data_M2[8][k])
		if o_data_M2[14][k] > percent_value:

			o_SAAW_NO2.append(o_data_M2[2][k])
			o_SAAW_NO3.append(o_data_M2[3][k])
			o_SAAW_O.append(o_data_M2[4][k])
			o_SAAW_PO4.append(o_data_M2[5][k])
			o_SAAW_salinity.append(o_data_M2[6][k])
			o_SAAW_SiO4.append(o_data_M2[7][k])
			o_SAAW_temp.append(o_data_M2[8][k])
		


	if len(o_ESSW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_ESSW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_ESSW NO2"+str(len(o_ESSW_NO2))+"points \n Mean = "+str(format((np.nanmean(o_ESSW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(o_ESSW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_ESSW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_ESSW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_ESSW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_ESSW NO3"+str(len(o_ESSW_NO3))+"points \n Mean = "+str(format((np.nanmean(o_ESSW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(o_ESSW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_ESSW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_ESSW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_ESSW_O ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_ESSW O "+str(len(o_ESSW_O))+"points \n Mean = "+str(format((np.nanmean(o_ESSW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(o_ESSW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_ESSW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_ESSW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_ESSW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_ESSW PO4 "+str(len(o_ESSW_PO4))+"points \n Mean = "+str(format((np.nanmean(o_ESSW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_ESSW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_ESSW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_ESSW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_ESSW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_ESSW SiO4 "+str(len(o_ESSW_SiO4))+"points \n Mean = "+str(format((np.nanmean(o_ESSW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_ESSW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_ESSW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_ESSW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_ESSW_temp ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_ESSW temp "+str(len(o_ESSW_temp))+"points \n Mean = "+str(format((np.nanmean(o_ESSW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(o_ESSW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_ESSW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_ESSW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_ESSW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_ESSW salinity "+str(len(o_ESSW_salinity))+"points \n Mean = "+str(format((np.nanmean(o_ESSW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(o_ESSW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_ESSW_salinity.svg",  format='svg', dpi=300)
		plt.close()



	if len(o_AAIW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_AAIW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_AAIW NO2"+str(len(o_AAIW_NO2))+"points \n Mean = "+str(format((np.nanmean(o_AAIW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(o_AAIW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_AAIW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_AAIW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_AAIW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_AAIW NO3"+str(len(o_AAIW_NO3))+"points \n Mean = "+str(format((np.nanmean(o_AAIW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(o_AAIW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_AAIW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_AAIW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_AAIW_O ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_AAIW O "+str(len(o_AAIW_O))+"points \n Mean = "+str(format((np.nanmean(o_AAIW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(o_AAIW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_AAIW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_AAIW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_AAIW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_AAIW PO4 "+str(len(o_AAIW_PO4))+"points \n Mean = "+str(format((np.nanmean(o_AAIW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_AAIW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_AAIW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_AAIW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_AAIW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_AAIW SiO4 "+str(len(o_AAIW_SiO4))+"points \n Mean = "+str(format((np.nanmean(o_AAIW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_AAIW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_AAIW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_AAIW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_AAIW_temp ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_AAIW temp "+str(len(o_AAIW_temp))+"points \n Mean = "+str(format((np.nanmean(o_AAIW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(o_AAIW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_AAIW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_AAIW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_AAIW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_AAIW salinity "+str(len(o_AAIW_salinity))+"points \n Mean = "+str(format((np.nanmean(o_AAIW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(o_AAIW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_AAIW_salinity.svg",  format='svg', dpi=300)
		plt.close()


	if len(o_PDW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_PDW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_PDW NO2"+str(len(o_PDW_NO2))+"points \n Mean = "+str(format((np.nanmean(o_PDW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(o_PDW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_PDW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_PDW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_PDW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_PDW NO3"+str(len(o_PDW_NO3))+"points \n Mean = "+str(format((np.nanmean(o_PDW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(o_PDW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_PDW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_PDW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_PDW_O ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_PDW O "+str(len(o_PDW_O))+"points \n Mean = "+str(format((np.nanmean(o_PDW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(o_PDW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_PDW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_PDW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_PDW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_PDW PO4 "+str(len(o_PDW_PO4))+"points \n Mean = "+str(format((np.nanmean(o_PDW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_PDW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_PDW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_PDW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_PDW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_PDW SiO4 "+str(len(o_PDW_SiO4))+"points \n Mean = "+str(format((np.nanmean(o_PDW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_PDW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_PDW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_PDW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_PDW_temp ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_PDW temp "+str(len(o_PDW_temp))+"points \n Mean = "+str(format((np.nanmean(o_PDW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(o_PDW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_PDW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_PDW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_PDW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_PDW salinity "+str(len(o_PDW_salinity))+"points \n Mean = "+str(format((np.nanmean(o_PDW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(o_PDW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_PDW_salinity.svg",  format='svg', dpi=300)
		plt.close()

	if len(o_STW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_STW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_STW NO2"+str(len(o_STW_NO2))+"points \n Mean = "+str(format((np.nanmean(o_STW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(o_STW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_STW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_STW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_STW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_STW NO3"+str(len(o_STW_NO3))+"points \n Mean = "+str(format((np.nanmean(o_STW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(o_STW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_STW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_STW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_STW_O ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_STW O "+str(len(o_STW_O))+"points \n Mean = "+str(format((np.nanmean(o_STW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(o_STW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_STW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_STW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_STW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_STW PO4 "+str(len(o_STW_PO4))+"points \n Mean = "+str(format((np.nanmean(o_STW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_STW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_STW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_STW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_STW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_STW SiO4 "+str(len(o_STW_SiO4))+"points \n Mean = "+str(format((np.nanmean(o_STW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_STW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_STW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_STW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_STW_temp ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_STW temp "+str(len(o_STW_temp))+"points \n Mean = "+str(format((np.nanmean(o_STW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(o_STW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_STW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_STW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_STW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_STW salinity "+str(len(o_STW_salinity))+"points \n Mean = "+str(format((np.nanmean(o_STW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(o_STW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_STW_salinity.svg",  format='svg', dpi=300)
		plt.close()


	if len(o_SAAW_NO2 ) > number_data:
		plt.xlim(range_NO2)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_SAAW_NO2 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_SAAW NO2"+str(len(o_SAAW_NO2))+"points \n Mean = "+str(format((np.nanmean(o_SAAW_NO2)), number_decimal) )+"\n std = "+str(format((np.nanstd(o_SAAW_NO2)), number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_SAAW_NO2.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_SAAW_NO3 ) > number_data:
		plt.xlim(range_NO3)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_SAAW_NO3 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_SAAW NO3"+str(len(o_SAAW_NO3))+"points \n Mean = "+str(format((np.nanmean(o_SAAW_NO3)),number_decimal))+"\n std = "+str(format((np.nanstd(o_SAAW_NO3)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_SAAW_NO3.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_SAAW_O ) > number_data:
		plt.xlim(range_oxigen)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_SAAW_O ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_SAAW O "+str(len(o_SAAW_O))+"points \n Mean = "+str(format((np.nanmean(o_SAAW_O)),number_decimal))+"\n std = "+str(format((np.nanstd(o_SAAW_O)),number_decimal)) ,  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_SAAW_O.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_SAAW_PO4 ) > number_data:
		plt.xlim(range_PO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_SAAW_PO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_SAAW PO4 "+str(len(o_SAAW_PO4))+"points \n Mean = "+str(format((np.nanmean(o_SAAW_PO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_SAAW_PO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_SAAW_PO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_SAAW_SiO4 ) > number_data:
		plt.xlim(range_SiO4)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_SAAW_SiO4 ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_SAAW SiO4 "+str(len(o_SAAW_SiO4))+"points \n Mean = "+str(format((np.nanmean(o_SAAW_SiO4)),number_decimal))+"\n std = "+str(format((np.nanstd(o_SAAW_SiO4)),number_decimal)), fontsize=histograms_fontsize)
		plt.savefig("ocean_o_SAAW_SiO4.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_SAAW_temp ) > number_data:
		plt.xlim(range_temp)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_SAAW_temp ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_SAAW temp "+str(len(o_SAAW_temp))+"points \n Mean = "+str(format((np.nanmean(o_SAAW_temp)),number_decimal))+"\n std = "+str(format((np.nanstd(o_SAAW_temp)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_SAAW_temp.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_SAAW_salinity ) > number_data:
		plt.xlim(range_sal)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_SAAW_salinity ,  facecolor="r", edgecolor="k")
		plt.title("ocean o_SAAW salinity "+str(len(o_SAAW_salinity))+"points \n Mean = "+str(format((np.nanmean(o_SAAW_salinity)),number_decimal))+"\n std = "+str(format((np.nanstd(o_SAAW_salinity)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("ocean_o_SAAW_salinity.svg",  format='svg', dpi=300)
		plt.close()


o_13C_v = np.loadtxt('13C_ocean.boat', skiprows=1, usecols=[2])
c_13C_v = np.loadtxt('13C_coast.boat', skiprows=1, usecols=[2])

o_13C_as_O_v = []
c_13C_as_O_v = []
o_13C_as_PO4_v = []
c_13C_as_PO4_v = []


o_13C_as_O_sal = []
c_13C_as_O_sal = []
o_13C_as_PO4_sal = []
c_13C_as_PO4_sal = []

o_13C_as_O_v_ESSW = []
c_13C_as_O_v_ESSW = []
o_13C_as_PO4_v_ESSW = []
c_13C_as_PO4_v_ESSW = []


o_13C_as_O_sal_ESSW = []
c_13C_as_O_sal_ESSW = []
o_13C_as_PO4_sal_ESSW = []
c_13C_as_PO4_sal_ESSW = []

o_13C_as_O_v_AAIW = []
c_13C_as_O_v_AAIW = []
o_13C_as_PO4_v_AAIW = []
c_13C_as_PO4_v_AAIW = []


o_13C_as_O_sal_AAIW = []
c_13C_as_O_sal_AAIW = []
o_13C_as_PO4_sal_AAIW = []
c_13C_as_PO4_sal_AAIW = []

o_13C_as_O_v_PDW = []
c_13C_as_O_v_PDW = []
o_13C_as_PO4_v_PDW = []
c_13C_as_PO4_v_PDW = []


o_13C_as_O_sal_PDW = []
c_13C_as_O_sal_PDW = []
o_13C_as_PO4_sal_PDW = []
c_13C_as_PO4_sal_PDW = []

o_13C_as_O_v_STW = []
c_13C_as_O_v_STW = []
o_13C_as_PO4_v_STW = []
c_13C_as_PO4_v_STW = []


o_13C_as_O_sal_STW = []
c_13C_as_O_sal_STW = []
o_13C_as_PO4_sal_STW = []
c_13C_as_PO4_sal_STW = []

o_13C_as_O_v_SAAW = []
c_13C_as_O_v_SAAW = []
o_13C_as_PO4_v_SAAW= []
c_13C_as_PO4_v_SAAW = []


o_13C_as_O_sal_SAAW = []
c_13C_as_O_sal_SAAW = []
o_13C_as_PO4_sal_SAAW = []
c_13C_as_PO4_sal_SAAW = []


if o_13C_as_O in   ('s','S','y','Y','O','o',1):


	for i in range(len(o_data_M2[0])):
		if isNaN(o_data_M2[9][i]) == 0:
			if isNaN(o_data_M2[6][i]) == 0:
				if isNaN(o_13C_v[i]) == 0:
					val= o_13C_v[i] - (1.6 -(0.0074 *o_data_M2[9][i]))
					o_13C_as_O_v.append(val)
					o_13C_as_O_sal.append(o_data_M2[6][i])

					if o_data_M2[10][i] > percent_value:
						o_13C_as_O_v_ESSW.append(val)
						o_13C_as_O_sal_ESSW.append(o_data_M2[6][i])

					if o_data_M2[11][i] > percent_value:
						o_13C_as_O_v_AAIW.append(val)
						o_13C_as_O_sal_AAIW.append(o_data_M2[6][i])

					if o_data_M2[12][i] > percent_value:
						o_13C_as_O_v_PDW.append(val)
						o_13C_as_O_sal_PDW.append(o_data_M2[6][i])

					if o_data_M2[13][i] > percent_value:
						o_13C_as_O_v_STW.append(val)
						o_13C_as_O_sal_STW.append(o_data_M2[6][i])

					if o_data_M2[14][i] > percent_value:
						o_13C_as_O_v_SAAW.append(val)
						o_13C_as_O_sal_SAAW.append(o_data_M2[6][i])
	if len(o_13C_as_O_v_ESSW) > number_data :
		plt.scatter(o_13C_as_O_sal_ESSW, o_13C_as_O_v_ESSW,marker= marker_ocean, c='m', zorder=2, edgecolor='k', s=40, label='ESSW')

	if len(o_13C_as_O_v_AAIW) > number_data :
		plt.scatter(o_13C_as_O_sal_AAIW, o_13C_as_O_v_AAIW,marker= marker_ocean, c='lime', zorder=3, edgecolor='k', s=40, label='AAIW')

	if len(o_13C_as_O_v_PDW) > number_data :
		plt.scatter(o_13C_as_O_sal_PDW, o_13C_as_O_v_PDW,marker= marker_ocean, c='r', zorder=4, edgecolor='k', s=40, label='PDW')

	if len(o_13C_as_O_v_STW) > number_data :
		plt.scatter(o_13C_as_O_sal_STW, o_13C_as_O_v_STW,marker= marker_ocean, c='c', zorder=5, edgecolor='k', s=40, label='STW')

	if len(o_13C_as_O_v_SAAW) > number_data :
		plt.scatter(o_13C_as_O_sal_SAAW, o_13C_as_O_v_SAAW,marker= marker_ocean, c='y', zorder=6, edgecolor='k', s=40, label='SAAW')

	

	plt.yticks(fontsize= scatter_fontsize)
	plt.xticks(fontsize= scatter_fontsize)
	plt.scatter(o_13C_as_O_sal, o_13C_as_O_v ,marker= marker_raw ,c='k', zorder=1, s=10, label='Raw data' )

	plt.legend(fontsize=12, markerscale=int(2))
	plt.xlim(sal_isotopic_x[0])
	plt.ylim(sal_isotopic_y[0])

	plt.savefig("oceanic_13C_as_O.svg",  format='svg', dpi=300)
	plt.close()


if c_13C_as_O in   ('s','S','y','Y','O','o',1):

	for i in range(len(c_data_M2[0])):
		if isNaN(c_data_M2[9][i]) == 0:
			if isNaN(c_data_M2[6][i]) == 0:
				if isNaN(c_13C_v[i]) == 0:
					val= c_13C_v[i] - (1.6 -(0.0074 *c_data_M2[9][i]))
					c_13C_as_O_v.append(val)
					c_13C_as_O_sal.append(c_data_M2[6][i])

					if c_data_M2[10][i] > percent_value:
						c_13C_as_O_v_ESSW.append(val)
						c_13C_as_O_sal_ESSW.append(c_data_M2[6][i])

					if c_data_M2[11][i] > percent_value:
						c_13C_as_O_v_AAIW.append(val)
						c_13C_as_O_sal_AAIW.append(c_data_M2[6][i])

					if c_data_M2[12][i] > percent_value:
						c_13C_as_O_v_PDW.append(val)
						c_13C_as_O_sal_PDW.append(c_data_M2[6][i])

					if c_data_M2[13][i] > percent_value:
						c_13C_as_O_v_STW.append(val)
						c_13C_as_O_sal_STW.append(c_data_M2[6][i])

					if c_data_M2[14][i] > percent_value:
						c_13C_as_O_v_SAAW.append(val)
						c_13C_as_O_sal_SAAW.append(c_data_M2[6][i])
	if len(c_13C_as_O_v_ESSW) > number_data :
		plt.scatter(c_13C_as_O_sal_ESSW, c_13C_as_O_v_ESSW,marker= marker_coast, c='m', zorder=2, edgecolor='k', s=40, label='ESSW')

	if len(c_13C_as_O_v_AAIW) > number_data :
		plt.scatter(c_13C_as_O_sal_AAIW, c_13C_as_O_v_AAIW,marker= marker_coast, c='lime', zorder=3, edgecolor='k', s=40, label='AAIW')

	if len(c_13C_as_O_v_PDW) > number_data :
		plt.scatter(c_13C_as_O_sal_PDW, c_13C_as_O_v_PDW,marker= marker_coast, c='r', zorder=4, edgecolor='k', s=40, label='PDW')

	if len(c_13C_as_O_v_STW) > number_data :
		plt.scatter(c_13C_as_O_sal_STW, c_13C_as_O_v_STW,marker= marker_coast, c='c', zorder=5, edgecolor='k', s=40, label='STW')

	if len(c_13C_as_O_v_SAAW) > number_data :
		plt.scatter(c_13C_as_O_sal_SAAW, c_13C_as_O_v_SAAW,marker= marker_coast, c='y', zorder=6, edgecolor='k', s=40, label='SAAW')

	plt.yticks(fontsize= scatter_fontsize)
	plt.xticks(fontsize= scatter_fontsize)
	plt.scatter(c_13C_as_O_sal, c_13C_as_O_v ,marker= marker_raw ,c='k', zorder=1,  s=10,label='Raw data' )
	plt.legend(fontsize=12,markerscale=int(2))
	plt.xlim(sal_isotopic_x[0])
	plt.ylim(sal_isotopic_y[0])
	plt.savefig("coastal_13C_as_O.svg",  format='svg', dpi=300)
	#plt.show()
	plt.close()

if o_13C_as_PO4 in ('s','S','y','Y','O','o',1):

	for i in range(len(o_data_M2[0])):
		if isNaN(o_data_M2[5][i]) == 0:
			if isNaN(o_data_M2[6][i]) == 0:
				if isNaN(o_13C_v[i]) == 0:
					val= o_13C_v[i] + ((o_data_M2[5][i]*1.1)-2.7)
					o_13C_as_PO4_v.append(val)
					o_13C_as_PO4_sal.append(o_data_M2[6][i])

					if o_data_M2[10][i] > percent_value:
						o_13C_as_PO4_v_ESSW.append(val)
						o_13C_as_PO4_sal_ESSW.append(o_data_M2[6][i])

					if o_data_M2[11][i] > percent_value:
						o_13C_as_PO4_v_AAIW.append(val)
						o_13C_as_PO4_sal_AAIW.append(o_data_M2[6][i])

					if o_data_M2[12][i] > percent_value:
						o_13C_as_PO4_v_PDW.append(val)
						o_13C_as_PO4_sal_PDW.append(o_data_M2[6][i])

					if o_data_M2[13][i] > percent_value:
						o_13C_as_PO4_v_STW.append(val)
						o_13C_as_PO4_sal_STW.append(o_data_M2[6][i])

					if o_data_M2[14][i] > percent_value:
						o_13C_as_PO4_v_SAAW.append(val)
						o_13C_as_PO4_sal_SAAW.append(o_data_M2[6][i])
	if len(o_13C_as_PO4_v_ESSW) > number_data :
		plt.scatter(o_13C_as_PO4_sal_ESSW, o_13C_as_PO4_v_ESSW,marker= marker_ocean, c='m', zorder=2, edgecolor='k', s=40, label='ESSW')

	if len(o_13C_as_PO4_v_AAIW) > number_data :
		plt.scatter(o_13C_as_PO4_sal_AAIW, o_13C_as_PO4_v_AAIW,marker= marker_ocean, c='lime', zorder=3, edgecolor='k', s=40, label='AAIW')

	if len(o_13C_as_PO4_v_PDW) > number_data :
		plt.scatter(o_13C_as_PO4_sal_PDW, o_13C_as_PO4_v_PDW,marker= marker_ocean, c='r', zorder=4, edgecolor='k', s=40, label='PDW')

	if len(o_13C_as_PO4_v_STW) > number_data :
		plt.scatter(o_13C_as_PO4_sal_STW, o_13C_as_PO4_v_STW,marker= marker_ocean, c='c', zorder=5, edgecolor='k', s=40, label='STW')

	if len(o_13C_as_PO4_v_SAAW) > number_data :
		plt.scatter(o_13C_as_PO4_sal_SAAW, o_13C_as_PO4_v_SAAW,marker= marker_ocean, c='y', zorder=6, edgecolor='k', s=40, label='SAAW')

	
	plt.yticks(fontsize= scatter_fontsize)
	plt.xticks(fontsize= scatter_fontsize)
	plt.scatter(o_13C_as_PO4_sal, o_13C_as_PO4_v ,marker= marker_raw ,c='k', zorder=1,  s=10,label='Raw data' )
	plt.legend(fontsize=12,markerscale=int(2))
	plt.xlim(sal_isotopic_x[0])
	plt.ylim(sal_isotopic_y[0])
	plt.savefig("oceanic_13C_as_PO4.svg",  format='svg', dpi=300)
	#plt.show()
	plt.close()

		
if c_13C_as_PO4 in ('s','S','y','Y','O','o',1):

	for i in range(len(c_data_M2[0])):
		if isNaN(c_data_M2[5][i]) == 0:
			if isNaN(c_data_M2[6][i]) == 0:
				if isNaN(c_13C_v[i]) == 0:
					val= c_13C_v[i] + ((c_data_M2[5][i]*1.1)-2.7)
					c_13C_as_PO4_v.append(val)
					c_13C_as_PO4_sal.append(c_data_M2[6][i])

					if c_data_M2[10][i] > percent_value:
						c_13C_as_PO4_v_ESSW.append(val)
						c_13C_as_PO4_sal_ESSW.append(c_data_M2[6][i])

					if c_data_M2[11][i] > percent_value:
						c_13C_as_PO4_v_AAIW.append(val)
						c_13C_as_PO4_sal_AAIW.append(c_data_M2[6][i])

					if c_data_M2[12][i] > percent_value:
						c_13C_as_PO4_v_PDW.append(val)
						c_13C_as_PO4_sal_PDW.append(c_data_M2[6][i])

					if c_data_M2[13][i] > percent_value:
						c_13C_as_PO4_v_STW.append(val)
						c_13C_as_PO4_sal_STW.append(c_data_M2[6][i])

					if c_data_M2[14][i] > percent_value:
						c_13C_as_PO4_v_SAAW.append(val)
						c_13C_as_PO4_sal_SAAW.append(c_data_M2[6][i])
	if len(c_13C_as_PO4_v_ESSW) > number_data :
		plt.scatter(c_13C_as_PO4_sal_ESSW, c_13C_as_PO4_v_ESSW,marker= marker_coast, c='m', zorder=2, edgecolor='k', s=40, label='ESSW')

	if len(c_13C_as_PO4_v_AAIW) > number_data :
		plt.scatter(c_13C_as_PO4_sal_AAIW, c_13C_as_PO4_v_AAIW,marker= marker_coast, c='lime', zorder=3, edgecolor='k', s=40, label='AAIW')

	if len(c_13C_as_PO4_v_PDW) > number_data :
		plt.scatter(c_13C_as_PO4_sal_PDW, c_13C_as_PO4_v_PDW,marker= marker_coast, c='r', zorder=4, edgecolor='k', s=40, label='PDW')

	if len(c_13C_as_PO4_v_STW) > number_data :
		plt.scatter(c_13C_as_PO4_sal_STW, c_13C_as_PO4_v_STW,marker= marker_coast, c='c', zorder=5, edgecolor='k', s=40, label='STW')

	if len(c_13C_as_PO4_v_SAAW) > number_data :
		plt.scatter(c_13C_as_PO4_sal_SAAW, c_13C_as_PO4_v_SAAW,marker= marker_coast, c='y', zorder=6, edgecolor='k', s=40, label='SAAW')

	
	plt.yticks(fontsize= scatter_fontsize)
	plt.xticks(fontsize= scatter_fontsize)
	plt.scatter(c_13C_as_PO4_sal, c_13C_as_PO4_v ,marker= marker_raw ,c='k', zorder=1,  s=10 ,label='Raw data')
	plt.legend(fontsize=12,markerscale=int(2))
	plt.xlim(sal_isotopic_x[0])
	plt.ylim(sal_isotopic_y[0])
	plt.savefig("coastal_13C_as_PO4.svg",  format='svg', dpi=300)
	plt.close()



if corrected_13C_histograms in ('s','S','y','Y','O','o',1):


	if len(o_13C_as_O_v_ESSW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_O_v_ESSW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_O_v_ESSW"+str(len(o_13C_as_O_v_ESSW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_O_v_ESSW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_O_v_ESSW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_O_v_ESSW.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_13C_as_PO4_v_ESSW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_PO4_v_ESSW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_PO4_v_ESSW"+str(len(o_13C_as_PO4_v_ESSW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_PO4_v_ESSW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_PO4_v_ESSW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_PO4_v_ESSW.svg",  format='svg', dpi=300)
		plt.close()	
	if len(o_13C_as_O_v_AAIW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_O_v_AAIW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_O_v_AAIW"+str(len(o_13C_as_O_v_AAIW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_O_v_AAIW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_O_v_AAIW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_O_v_AAIW.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_13C_as_PO4_v_AAIW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_PO4_v_AAIW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_PO4_v_AAIW"+str(len(o_13C_as_PO4_v_AAIW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_PO4_v_AAIW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_PO4_v_AAIW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_PO4_v_AAIW.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_13C_as_O_v_PDW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_O_v_PDW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_O_v_PDW"+str(len(o_13C_as_O_v_PDW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_O_v_PDW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_O_v_PDW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_O_v_PDW.svg",  format='svg', dpi=300)
		plt.close()

	if len(o_13C_as_PO4_v_PDW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_PO4_v_PDW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_PO4_v_PDW"+str(len(o_13C_as_PO4_v_PDW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_PO4_v_PDW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_PO4_v_PDW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_PO4_v_PDW.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_13C_as_O_v_STW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_O_v_STW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_O_v_STW"+str(len(o_13C_as_O_v_STW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_O_v_STW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_O_v_STW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_O_v_STW.svg",  format='svg', dpi=300)
		plt.close()	
	if len(o_13C_as_PO4_v_STW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_PO4_v_STW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_PO4_v_STW"+str(len(o_13C_as_PO4_v_STW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_PO4_v_STW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_PO4_v_STW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_PO4_v_STW.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_13C_as_O_v_SAAW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_O_v_SAAW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_O_v_SAAW"+str(len(o_13C_as_O_v_SAAW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_O_v_SAAW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_O_v_SAAW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_O_v_SAAW.svg",  format='svg', dpi=300)
		plt.close()
	if len(o_13C_as_PO4_v_SAAW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(o_13C_as_PO4_v_SAAW ,  facecolor="r", edgecolor="k")
		plt.title("o_13C_as_PO4_v_SAAW"+str(len(o_13C_as_PO4_v_SAAW))+"points \n Mean = "+str(format((np.nanmean(o_13C_as_PO4_v_SAAW)),number_decimal))+"\n std = "+str(format((np.nanstd(o_13C_as_PO4_v_SAAW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("o_13C_as_PO4_v_SAAW.svg",  format='svg', dpi=300)
		plt.close()

	if len(c_13C_as_O_v_ESSW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_O_v_ESSW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_O_v_ESSW"+str(len(c_13C_as_O_v_ESSW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_O_v_ESSW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_O_v_ESSW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_O_v_ESSW.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_13C_as_PO4_v_ESSW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_PO4_v_ESSW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_PO4_v_ESSW"+str(len(c_13C_as_PO4_v_ESSW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_PO4_v_ESSW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_PO4_v_ESSW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_PO4_v_ESSW.svg",  format='svg', dpi=300)
		plt.close()	
	if len(c_13C_as_O_v_AAIW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_O_v_AAIW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_O_v_AAIW"+str(len(c_13C_as_O_v_AAIW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_O_v_AAIW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_O_v_AAIW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_O_v_AAIW.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_13C_as_PO4_v_AAIW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_PO4_v_AAIW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_PO4_v_AAIW"+str(len(c_13C_as_PO4_v_AAIW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_PO4_v_AAIW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_PO4_v_AAIW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_PO4_v_AAIW.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_13C_as_O_v_PDW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_O_v_PDW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_O_v_PDW"+str(len(c_13C_as_O_v_PDW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_O_v_PDW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_O_v_PDW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_O_v_PDW.svg",  format='svg', dpi=300)
		plt.close()

	if len(c_13C_as_PO4_v_PDW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_PO4_v_PDW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_PO4_v_PDW"+str(len(c_13C_as_PO4_v_PDW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_PO4_v_PDW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_PO4_v_PDW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_PO4_v_PDW.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_13C_as_O_v_STW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_O_v_STW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_O_v_STW"+str(len(c_13C_as_O_v_STW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_O_v_STW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_O_v_STW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_O_v_STW.svg",  format='svg', dpi=300)
		plt.close()	
	if len(c_13C_as_PO4_v_STW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_PO4_v_STW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_PO4_v_STW"+str(len(c_13C_as_PO4_v_STW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_PO4_v_STW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_PO4_v_STW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_PO4_v_STW.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_13C_as_O_v_SAAW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_O_v_SAAW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_O_v_SAAW"+str(len(c_13C_as_O_v_SAAW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_O_v_SAAW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_O_v_SAAW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_O_v_SAAW.svg",  format='svg', dpi=300)
		plt.close()
	if len(c_13C_as_PO4_v_SAAW) > number_data:
		plt.xlim(range_13C_corrected)
		plt.yticks(fontsize= histograms_fontsize)
		plt.xticks(fontsize= histograms_fontsize)
		plt.hist(c_13C_as_PO4_v_SAAW ,  facecolor="r", edgecolor="k")
		plt.title("c_13C_as_PO4_v_SAAW"+str(len(c_13C_as_PO4_v_SAAW))+"points \n Mean = "+str(format((np.nanmean(c_13C_as_PO4_v_SAAW)),number_decimal))+"\n std = "+str(format((np.nanstd(c_13C_as_PO4_v_SAAW)),number_decimal)),  fontsize=histograms_fontsize)
		plt.savefig("c_13C_as_PO4_v_SAAW.svg",  format='svg', dpi=300)
		plt.close()


print("                      . .     ")
print("                    '.-:-.`   ")
print("                    '  :  `   ")
print("                 .-----:      ")
print("               .'       `.    ")
print("         ,    /       (o) \   ")
print("         \`._/          ,__)  ")
print("     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

