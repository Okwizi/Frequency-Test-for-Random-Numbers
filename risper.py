from fractions import Fraction
import math

def calculate_utilization(arrival_rate, service_rate):
    return arrival_rate / service_rate

def calculate_expected_number_in_queue(arrival_rate, service_rate):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return (utilization**2) / (1 - utilization)

def calculate_expected_waiting_time_in_queue(arrival_rate, service_rate):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return utilization / (service_rate * (1 - utilization))

def calculate_expected_number_in_system(arrival_rate, service_rate):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return utilization / (1 - utilization)

def calculate_expected_waiting_time_in_system(arrival_rate, service_rate):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return 1 / (service_rate * (1 - utilization))

def calculate_probability_of_wait(arrival_rate, service_rate):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return utilization

def calculate_probability_of_n_units_in_system(n, arrival_rate, service_rate):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return ((utilization ** n) * math.exp(-utilization)) / math.factorial(n)

def calculate_probability_of_no_wait(arrival_rate, service_rate):
    return 1 - calculate_probability_of_wait(arrival_rate, service_rate)

def calculate_probability_of_more_than_n_units_in_system(n, arrival_rate, service_rate):
    probability = 1
    for i in range(n):
        probability -= calculate_probability_of_n_units_in_system(i, arrival_rate, service_rate)
    return probability

def calculate_probability_of_wait_more_than_threshold(arrival_rate, service_rate, threshold):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return 1 - sum(calculate_probability_of_n_units_in_system(i, arrival_rate, service_rate) for i in range(threshold))

def calculate_flow_increase_for_second_booth(arrival_rate, service_rate):
    utilization = calculate_utilization(arrival_rate, service_rate)
    return (1 / (2 - utilization)) - (1 / (1 - utilization))

arrival_rate_str = input("Enter arrival rate (per minute, in fraction format e.g., 1/8): ")
service_rate_str = input("Enter service rate (per minute, in fraction format e.g., 1/4): ")

arrival_rate = Fraction(arrival_rate_str)
service_rate = Fraction(service_rate_str)

print("a) Expected fraction of the day that the phone will be in use:", calculate_utilization(arrival_rate, service_rate))
print("b) Expected number of units in the queue:", calculate_expected_number_in_queue(arrival_rate, service_rate))
print("c) Expected waiting time in the queue:", calculate_expected_waiting_time_in_queue(arrival_rate, service_rate))
print("e) Expected number of units in the system:", calculate_expected_number_in_system(arrival_rate, service_rate))
print("f) Expected waiting time in the system:", calculate_expected_waiting_time_in_system(arrival_rate, service_rate))
print("g) Probability that an arrival will have to wait in queue for service:", calculate_probability_of_wait(arrival_rate, service_rate))
print("h) Probability that exactly 3 units are in the system:", calculate_probability_of_n_units_in_system(3, arrival_rate, service_rate))
print("i) Probability that an arrival will not have to wait in queue for service:", calculate_probability_of_no_wait(arrival_rate, service_rate))
print("j) Probability that there are 3 or more units in the system:", calculate_probability_of_more_than_n_units_in_system(3, arrival_rate, service_rate))

print("k) Probability that an arrival will have to wait more than 6 min in queue for service:", 
      calculate_probability_of_wait_more_than_threshold(arrival_rate, service_rate, 6))

print("l) Probability that more than 5 units in system:", 
      calculate_probability_of_more_than_n_units_in_system(5, arrival_rate, service_rate))

print("m) Probability that an arrival will have to wait more than 8 min in system:", 
      calculate_probability_of_wait_more_than_threshold(arrival_rate, service_rate, 8) * calculate_utilization(arrival_rate, service_rate))

print("n) Telephone company will install a second booth when convinced that an arrival would have to wait for at least 6 min in queue for phone. By how much the flow of arrival is increased in order to justify a second booth:",
      calculate_flow_increase_for_second_booth(arrival_rate, service_rate))
