# The data we need to retrive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Declaring a new list
candidate_options =[]
# Declaring an empty dictionary
candidate_votes ={}
# Declaring a county list
county = []
county_votes = {}

#County with larger turnout
largest_county = ""
largest_county_votes = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Read and print the header row.
     headers = next(file_reader)
     
     # Print each row in the CSV file.
     for row in file_reader:
          # Add to the total vote count.
          total_votes += 1
          # Print the candidate name from each row
          candidate_name = row[2]
          
          # Conditional to avoid repeating names in the list
          if candidate_name not in candidate_options:

               # Adding canidate name to the list
               candidate_options.append(candidate_name)

               # Begin tracking that candidate's vote count.
               candidate_votes[candidate_name] = 0

          # Add a vote to that candidate's count.
          candidate_votes[candidate_name] += 1     

          # Get county name for each row
          county_name = row[1]

          # Conditional to avoid repeating county names in the list
          if county_name not in county:
               county.append(county_name)

               # Initializing county vote to zero
               county_votes[county_name] = 0
          # Add a vote to the county     
          county_votes[county_name] += 1


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Print the final vote count to the terminal.
     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")
     print(election_results, end="")
          
     # Save the final vote count to the text file.
     txt_file.write(election_results)

     county_title = (f"\nCounty Votes:\n")
     print(county_title)
     txt_file.write(county_title)


          # Iterate through the county list
     for county_name in county_votes:

          # Retrieve the count of each county
          c_votes = county_votes[county_name]
          # Calculate procentage of county votes
          c_vote_percentage = float(c_votes) / float(total_votes) * 100

          county_results = (f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
          print(county_results)
          txt_file.write(county_results)

          # Determine largest county and largest county votes
          if c_votes > largest_county_votes:
               largest_county_votes = c_votes
               largest_county = county_name
     
     largest_county_results = (
               f"\n-------------------------\n"
               f"Largest County Turnout: {largest_county}\n"
               f"-------------------------\n"
               )

     print(largest_county_results)
     txt_file.write(largest_county_results)


     # Iterate through the candidate list
     for candidate_name in candidate_votes:

          # Retrieve the count of a candidate
          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100
          # Print the candidate name and percentage of votes.
          candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          # Print each candidate, their voter count, and percentage to the terminal.
          print(candidate_results)
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)
               
          # Determine winning vote count, winning percentage, and candidate.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               winning_count = votes
               winning_percentage = vote_percentage
               winning_candidate = candidate_name
 
     winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
     print(winning_candidate_summary)

     # Save the winning candidate's name to the text file.
     txt_file.write(winning_candidate_summary)