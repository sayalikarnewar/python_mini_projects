#take dataset of 100 values and find mean median mode and midrange
import numpy
import collections
total = [1,2,3,4,2,4,5,3,2,4,2,4,11,33,44,23,33,2,67,8,5,88,77,5,4,45,4,45,5,50,70,73,45,34,67,83,23,11,47,46,78,46,12,98,64,89,53,7,44,35,56]

dataset = numpy.array(total)
print("total dataset values : ",numpy.count_nonzero(dataset))


'''for i in dataset:
	sum += sum + dataset[i]
'''
print("mean of dataset values : ",sum(dataset)/numpy.count_nonzero(dataset))

#print(numpy.sort(dataset))

print("median of dataset values : ",numpy.median(dataset))

#mode = collections.Counter(dataset)

print("mode of dataset values : " ,max(total,key=total.count))

'''
sort = sorted(total)
min = sort[0:1]
max = sort[-1]'''
x = max(dataset)
print(x)

print("midrange of dataset values : ",(min(dataset)+max(dataset))/2)
