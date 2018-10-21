from Imgflow import resize
import math



def percentile(data_list, score, kind='weak'):

	n = len(data_list)

	if kind == 'strict':
		return len([i for i in data_list if i < score]) / float(n) * 100
	elif kind == 'weak':
		return len([i for i in data_list if i <= score]) / float(n) * 100
	elif kind == 'mean':
		return (len([i for i in data_list if i < score]) + len([i for i in data_list if i <= score])) * 50 / float(n)
	else:
		raise ValueError("Ne ok.")


def decile(array, score, kind='weak'):

	if not isinstance(array, list):
		raise TypeError('first value input must be a list')
	percentile_score = percentile(array, score, kind=kind)
	if percentile_score == 100.0:
		return 10
	else:
		decile = int(percentile_score * 0.1) + 1
		return decile


def mean(data_list):

	#data_list = map(float, data_list)
	return sum(data_list) / len(data_list)

def standard_deviation(data_list):

	data_list = map(float, data_list)
	mean = calculate.mean(data_list)

	deviations = [i - mean for i in data_list]
	deviations_squared = [math.pow(i, 2) for i in deviations]

	mean_deviation = mean(deviations_squared)
	standard_deviation = math.sqrt(mean_deviation)

	return standard_deviation


def calc(image,alpha):

	l= 328*mean(alpha)
	h = math.tan(l)
	im = resize(image,h)

	return im
