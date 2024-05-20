from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("DataFrameExample") \
    .getOrCreate()

# Create sample data
data = [("John", 25), ("Alice", 30), ("Bob", 35)]
columns = ["Name", "Age"]

# Create a DataFrame from a list of tuples
df = spark.createDataFrame(data, columns)

# Show the DataFrame
print("Original DataFrame:")
df.show()

# Filter the DataFrame to select people older than 30
df_filtered = df.filter(df["Age"] > 30)

# Show the filtered DataFrame
print("Filtered DataFrame:")
df_filtered.show()

# Stop SparkSession
spark.stop()