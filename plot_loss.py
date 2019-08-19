# Plot Loss
import numpy as np 
import pandas as pd 
import os
import sys
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------------------------------------------

def plot_loss(train_statistics_path):
	train_statistics_df = pd.read_csv(train_statistics_path,sep='\t')
	print(train_statistics_df.head(20))

	epoch_list = list(train_statistics_df['Epoch'])
	train_loss_list = list(train_statistics_df['Training Loss'])
	val_loss_list = list(train_statistics_df['Validation Loss'])

	#print(len(epoch_list))
	#print(len(train_loss_list))
	#print(len(val_loss_list))

	plt.plot(epoch_list,train_loss_list, c='brown', label='Training_Loss')
	plt.plot(epoch_list,val_loss_list, c='green', label='Validation_Loss')
	plt.title('Epoch v Loss Plot')
	plt.xlabel('Epochs')
	plt.ylabel('Model Loss')
	plt.legend()
	plt.grid()
	plt.savefig('./loss_plot.png')

#-------------------------------------------------------------------------------------------------------------------------------------

def plot_accuracy(train_statistics_path):

	train_statistics_df = pd.read_csv(train_statistics_path,sep='\t')
	print(train_statistics_df.head(20))

	epoch_list = list(train_statistics_df['Epoch'])
	train_acc_list = list(train_statistics_df['Training Accuracy'])
	val_acc_list = list(train_statistics_df['Validation Accuracy'])

	#print(len(epoch_list))
	#print(len(train_acc_list))
	#print(len(val_acc_list))

	plt.plot(epoch_list,train_acc_list, c='brown', label='Training_Accuracy')
	plt.plot(epoch_list,val_acc_list, c='green', label='Validation_Accuracy')
	plt.title('Epoch v Accuracy Plot')
	plt.xlabel('Epochs')
	plt.ylabel('Model Accuracy')
	plt.legend()
	plt.grid()
	plt.savefig('./accuracy_plot.png')

#----------------------------------------------------------------------------------------------------------------------------------------

def main():
	train_statistics_path = '/home/ayush/Activity_Recognition/Action-Recognition/train_statistics.csv'
	plot_loss(train_statistics_path)
	#plot_accuracy(train_statistics_path)




if __name__ == '__main__':
	main()