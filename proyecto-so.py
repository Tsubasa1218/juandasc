#!/usr/bin/python
from flask import Flask, jsonify, make_response, request
import subprocess

app = Flask(__name__)

#Index message, Welcome LUL
@app.route('/', methods = ['GET'])
def index():
	Salida = "Bienvenido al gestor de VMs de SO\nIntegrantes: \n\tJuan David Suaza \n\tJuan Jose Salazar \n\tJuan Jose Varela\n"	
	return Salida
@app.route('/ostypes', methods = ['GET'])
def ostypes():
	lista = subprocess.check_output(['VBoxManage', 'list', 'ostypes'])
	return lista

@app.route('/vms', methods = ['GET'])
def listvms():
	lista = subprocess.check_output(['VBoxManage', 'list', 'vms'])
	return lista

@app.route('/vms/running', methods = ['GET'])
def listrunningvms():
	lista = subprocess.check_output(['VBoxManage', 'list', 'runningvms'])
	return lista 

@app.route('/vms/info/<nombre>', methods = ['GET'])
def getVM(nombre):
	vbox1 =	subprocess.Popen(['VBoxManage', 'showvminfo', nombre], stdout = subprocess.PIPE)
	grepCPU = subprocess.check_output(['grep', 'Number of CPUs'], stdin = vbox1.stdout)
	vbox2 =	subprocess.Popen(['VBoxManage', 'showvminfo', nombre], stdout = subprocess.PIPE)
	grepRAM = subprocess.check_output(['grep', 'VRAM size'], stdin = vbox2.stdout)
	vbox3 =	subprocess.Popen(['VBoxManage', 'showvminfo', nombre], stdout = subprocess.PIPE)	
	grepNET = subprocess.check_output(['grep', 'Attachment'], stdin = vbox3.stdout)
	output = grepCPU + "\n" + grepRAM + "\n" + grepNET + "\n" 	
	return output

@app.route('/create', methods = ['POST'])
def createVM():		

	nombre = request.json['nombre']
	ram = request.json['ram']
	cpu = request.json['cpu']
	
	output = subprocess.check_output(['./scriptCrear.sh', nombre, ram, cpu])
	return output

@app.route('/delete/<nombre>', methods = ['DELETE'])
def deleteVM(nombre):
	borrarVM = subprocess.check_output(['VBoxManage', 'unregistervm', nombre, '--delete'])
	return "Borrada " + nombre	
if __name__ == '__main__':
	app.run(debug = False, host = '127.0.0.1')
