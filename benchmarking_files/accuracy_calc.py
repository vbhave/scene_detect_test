import numpy as np
predicted = np.loadtxt(fname="properly_got_results.txt", dtype='int')
#print(predicted)

actual = np.loadtxt(fname='ground_truth_formatted.txt', dtype='int')
#print(actual)

#print(predicted.shape)
#print(actual.shape)

num_images = predicted.shape[0]

cequal1 = 0
cequal2 = 0
cequal3 = 0
cequal4 = 0
cequal5 = 0

for i in range(predicted.shape[0]):
	if predicted[i][0] == actual[i]:
		cequal1 += 1
	elif predicted[i][1] == actual[i]:
		cequal2 += 1
	elif predicted[i][2] == actual[i]:
		cequal3 += 1
	elif predicted[i][3] == actual[i]:
		cequal4 += 1
	elif predicted[i][4] == actual[i]:
		cequal5 += 1

cequal2 += cequal1
cequal3 += cequal2
cequal4 += cequal3
cequal5 += cequal4

print("Top 1 accuracy is " , str(cequal1 / num_images), " with ", str(cequal1), " images correctly predicted")
print("Top 2 accuracy is " , str(cequal2 / num_images), " with ", str(cequal2), " images correctly predicted")
print("Top 3 accuracy is " , str(cequal3 / num_images), " with ", str(cequal3), " images correctly predicted")
print("Top 4 accuracy is " , str(cequal4 / num_images), " with ", str(cequal4), " images correctly predicted")
print("Top 5 accuracy is " , str(cequal5 / num_images), " with ", str(cequal5), " images correctly predicted")

true_positives = np.zeros(365, dtype='int')
false_positives = np.zeros(365, dtype='int')
false_negatives = np.zeros(365, dtype='int')

for i in range(predicted.shape[0]):
	if predicted[i][0] == actual[i]:
		true_positives[actual[i]] += 1
	else:
		false_positives[predicted[i][0]] += 1
		false_negatives[actual[i]] += 1

#print("True positives")
#print(true_positives)
#print("false_positives")
#print(false_positives)
#print("false_negatives")
#print(false_negatives)

precision = true_positives / ( true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)

#print("precision")
#print(precision)
#print("recall")
#print(recall)

f1_score = (2 * precision * recall) / (precision + recall)
print("f1_score")

print(precision[89])
print(precision[202])
print(precision[240])
print(precision[268])
print(precision[269])

print(recall[89])
print(recall[202])
print(recall[240])
print(recall[268])
print(recall[269])

#print(f1_score)

'''print("Best Performance")
f1_sorted_index = np.argsort(-f1_score)
for i in range(10):
	print("score is ", f1_score[f1_sorted_index[i]], " at index   ", str(f1_sorted_index[i]), "having  ", true_positives[f1_sorted_index[i]], "  true positives, ", false_positives[f1_sorted_index[i]], "  false positives and  ", false_negatives[f1_sorted_index[i]], " false negatives.")


print("Worst Performance")
f1_sorted_index = np.argsort(f1_score)
for i in range(10):
	print("score is ", f1_score[f1_sorted_index[i]], " at index   ", str(f1_sorted_index[i]), "having  ", true_positives[f1_sorted_index[i]], "  true positives, ", false_positives[f1_sorted_index[i]], "  false positives and  ", false_negatives[f1_sorted_index[i]], " false negatives.")
'''
'''
recall_score_sum = 0
count = 0
fcheck = open('IO_places365.txt','r')
fcheck_lines = fcheck.readlines()
recall_score = np.nan_to_num(f1_score)
#print(f1_score)
recall_int = recall_score.astype(float)
#print(f1_int)

for i in range(365):
	#print(fcheck_lines[i].strip().split(' ')[1])
	if fcheck_lines[i].strip().split()[1] == "1":
		#print("in count")
		count += 1
		#print(f1_int[i])
		recall_score_sum += recall_int[i]

print(count)
print("f1 score is  ")
print(recall_score_sum)
print("f1 average is ")
print(recall_score_sum / count)
'''



'''f1 = open("results.txt", "r")
f2 = open("places365_val.txt","r")
content1 = f1.readlines()
content2 = f2.readlines()
cequal1 = 0
cequal2 = 0
cequal3 = 0
cequal4 = 0
cequal5 = 0

num_images = 15000
for i in range(num_images):
	#print(str(content2[i].split(' ')[1]) + "  and predicted is " + str(content1[i]))
	#print(content2[i].split(' ')[1])
	#print(content1[i].split('\t')[0])
	#print(content1[i].split('\t')[1])
	#print(content1[i].split('\t')[2])
	if content2[i].split(' ')[1].strip() == content1[i].split('\t')[0].strip():
		cequal1 += 1
		#print("in equal 1")
	elif content2[i].split(' ')[1].strip() == content1[i].split('\t')[1].strip():
		cequal2 += 1
		#print("in equal 2")
	elif content2[i].split(' ')[1].strip() == content1[i].split('\t')[2].strip():
		cequal3 += 1
	elif content2[i].split(' ')[1].strip() == content1[i].split('\t')[3].strip():
		cequal4 += 1
	elif content2[i].split(' ')[1].strip() == content1[i].split('\t')[4].strip():
		cequal5 += 1
	
#print("in equal 3")	
cequal2 += cequal1
cequal3 += cequal2
cequal4 += cequal3
cequal5 += cequal4

print("Top 1 accuracy is " , str(cequal1 / num_images), " with ", str(cequal1), " images correctly predicted")
print("Top 2 accuracy is " , str(cequal2 / num_images), " with ", str(cequal2), " images correctly predicted")
print("Top 3 accuracy is " , str(cequal3 / num_images), " with ", str(cequal3), " images correctly predicted")
print("Top 4 accuracy is " , str(cequal4 / num_images), " with ", str(cequal4), " images correctly predicted")
print("Top 5 accuracy is " , str(cequal5 / num_images), " with ", str(cequal5), " images correctly predicted")

#print("Got ", count_equal, "correct out of 2000 total images, thus having an accuracy of  ", str(count_equal / 2000))
'''
