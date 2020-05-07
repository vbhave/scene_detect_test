fpredict = open('full_model_results.txt','r')
factual = open('places365_val.txt','r')
correct = [[0] * 365]
predict_correct = [[0] * 365]

#print(matrix)

num_lines = 15000
predict_lines = fpredict.readlines()
actual_lines = factual.readlines()
for i in range(num_lines):
	predict_content = predict_lines[i].strip()
	actual_content = actual_lines[i].strip()
	#print(predict_content)
	#print(actual_content)
	actual_value = actual_content.split(' ')[1]
	#print(int(actual_value))
	predict_value = predict_content.split('\t')[0]
	#print(int(predict_value))
	if actual_value == predict_value:
		matrix[0][int(actual_value)] += 1
		#print(actual_value)
	else:
		matrix[1][int(actual_value)] += 1
		
#print(matrix)

for i in range(365):
	matrix[2][int(actual_value)] = matrix[0][int(actual_value)] / matrix[1][int(actual_value)]

print(matrix)
