#thankdrop, commaseparating delegations
#execute thankdrop calcs
#this will be used in a lottery for 1 and only nft,
#objective is to say thanks in including us in the contest from march
#organized by sunshine validation


import json
import pandas as pd



def thankyou(jsonfile,threshold):
	stringedListEligibles=[]
	#importing a sample response from RPC query in .json format
	data = json.load(open(jsonfile))

	#example is done for huahua
	thresholdTokens=threshold

	#we know all data is contained in delegation_responses
	for i in range(len(data["delegation_responses"])):
		#then jumping i and i+1 through every delegate
		delegationResponse=data["delegation_responses"][i]['delegation']
		#print(delegationResponse)
		sharesStaked=round(float(delegationResponse["shares"])/1e6,2)
		#1e6 because the unit is u-huahua/u-juno, etc...
		
		addressStaked=delegationResponse["delegator_address"]
		if sharesStaked >= thresholdTokens:
			print(addressStaked+"|"+str(sharesStaked) + "|"+jsonfile+"\n")
			stringedListEligibles.append(addressStaked+"|"+str(sharesStaked) + "|"+jsonfile+"\n")

	with open("Output_eligible.txt", "a+") as text_file:
		for eachEligible in stringedListEligibles:
			text_file.write(eachEligible)
