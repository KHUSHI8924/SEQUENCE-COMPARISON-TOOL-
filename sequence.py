import matplotlib.pyplot as plt

def sequence_identity(seq1,seq2):

    seq1 = seq1.upper()
    seq2 = seq2.upper()
    
    matches = 0
    mismatches = []
    
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            matches +=1
        else:
            mismatches.append(i+1)
            
    Identity= (matches/ len(seq1)) *100
    return Identity, mismatches 
   
seq1 = input("Enter the first sequence: ")
seq2 = input("Enter the second sequence: ")

if len(seq1) != len(seq2): 
    print("Error!! Sequence must be of same length for comparison.")
else:
    Identity, mismatches= sequence_identity(seq1, seq2)
    print(f"\nSequence Identity: {Identity:}%")
    if mismatches:
        print(f"Mismatches at positions: {mismatches}")
    else:
        print("Mismatches at positions: None")
        
    
# VISUALIZATION 
colors = ['blue' if seq1[i] == seq2[i] else 'pink' for i in range(len(seq1))]
positions = range(1, len(seq1)+1)

plt.figure(figsize=(10,8))
plt.bar(positions, [1]*len(seq1), color=colors, edgecolor='black')
plt.title(f"Sequence comparison (Identity: {Identity:}%)")
plt.xlabel("Position")
plt.yticks([])
plt.show()
    
    
    
    
    
    
    
   
