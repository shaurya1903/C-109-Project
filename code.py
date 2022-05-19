import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
Math_marks= df["math score"].to_list()
Reading_marks=df["reading score"].to_list()
Writing_marks=df["writing score"].to_list()

math_mean = statistics.mean(Math_marks)
reading_mean = statistics.mean(Reading_marks)
writing_mean= statistics.mean(Writing_marks)

math_median = statistics.median(Math_marks)
reading_median = statistics.median(Reading_marks)
writing_median = statistics.median(Writing_marks)

math_mode = statistics.mode(Math_marks)
reading_mode = statistics.mode(Reading_marks)
writing_mode = statistics.mode(Writing_marks)

print("Mean, Median and Mode of marks in math is {}, {} and {} respectively".format(math_mean,math_median,math_mode))
print("Mean, Median and Mode of marks in reading is {}, {} and {} respectively".format(reading_mean,reading_median,reading_mode))
print("Mean, Median and Mode of marks in writing is {}, {} and {} respectively".format(writing_mean,writing_median,writing_mode))

math_std_deviation = statistics.stdev(Math_marks)
reading_std_deviation = statistics.stdev(Reading_marks)
writing_std_deviation = statistics.stdev(Writing_marks)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

math_list_of_data_within_1_std_deviation = [result for result in Math_marks if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in Math_marks if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in Math_marks if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

reading_list_of_data_within_1_std_deviation = [result for result in Reading_marks if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in Reading_marks if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in Reading_marks if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_list_of_data_within_1_std_deviation = [result for result in Writing_marks if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in Writing_marks if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in Writing_marks if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(Math_marks)))
print("{}% of data for the marks scored in math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(Math_marks)))
print("{}% of data for the marks scored in math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(Math_marks)))

print("{}% of data for the marks scored in reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(Reading_marks)))
print("{}% of data for the marks scored in reading within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(Reading_marks)))
print("{}% of data for the marks scored in reading within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(Reading_marks)))

print("{}% of data for the marks scored in writing lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(Writing_marks)))
print("{}% of data for the marks scored in writing lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(Writing_marks)))
print("{}% of data for the marks scored in writing lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(Writing_marks)))
