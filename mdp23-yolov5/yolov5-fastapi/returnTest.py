import subprocess
import readID

def returnTest():
	# subprocess.run('script-startserver.sh', shell=True, check=True) 
	# print("Server up!")
	subprocess.run('script-rundetection.sh', shell=True, check=True)
	print("Detection done!") 

returnTest()