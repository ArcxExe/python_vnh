import timeit
                    
code_to_measure = """
for i in range(1000):
    pass
"""

execution_time = timeit.timeit(stmt=code_to_measure, number=1000)
print(f"Execution time: {execution_time} seconds")

                
