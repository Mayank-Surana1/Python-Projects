# is a classic mathematical puzzle involving three rods (A, B, and C) and n disks of different sizes. 
#Initially, all disks are stacked on rod A in decreasing order of diameter - the largest disk at the bottom and the smallest at the top.
# Goal is to move the entire stack to another rod (rod C) while following these rules:

# Move only one disk at a time.
# 1. At each step, you can take the top disk from any rod and place it on another rod.
# 2. A disk can only be moved if it is the topmost disk of a rod.
# 3. No larger disk may be placed on top of a smaller disk.
def tower_of_hanoi(n, source='A', destination='C', auxiliary='B', towers=None, moves=None):
        # Initialize towers and moves list on first call
        if towers is None:
            towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
            moves = []
        
        # Base case: move single disk from source to destination
        if n == 1:
            disk = towers[source].pop()
            towers[destination].append(disk)
            moves.append((source, destination, disk))
            display_towers(towers, moves[-1])
            return moves
        
        # Recursive step 1: move n-1 disks from source to auxiliary using destination
        tower_of_hanoi(n - 1, source, auxiliary, destination, towers, moves)
        
        # Move the largest disk from source to destination
        disk = towers[source].pop()
        towers[destination].append(disk)
        moves.append((source, destination, disk))
        display_towers(towers, moves[-1])
        
        # Recursive step 2: move n-1 disks from auxiliary to destination using source
        tower_of_hanoi(n - 1, auxiliary, destination, source, towers, moves)
        
        return moves

def display_towers(towers, last_move):
    print(f"\nMove disk {last_move[2]} from Tower {last_move[0]} to Tower {last_move[1]}")
    print("=" * 40)
    
    max_height = max(len(v) for v in towers.values())
    
    for level in range(max_height, 0, -1):
        for tower_name in ['A', 'B', 'C']:
            if len(towers[tower_name]) >= level:
                disk = towers[tower_name][level - 1]
                print(f"  {disk:^6}", end=" ")
            else:
                print(f"  {'|':^6}", end=" ")
        print()
    
    print("  " + "-" * 20)
    print("   A      B      C")

def main():
    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            print("Number of disks must be positive!")
            return
        
        print(f"\nSolving Tower of Hanoi with {n} disks...\n")
        print("Initial State:")
        towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
        display_initial(towers)
        
        moves = tower_of_hanoi(n)
        print(f"\n✓ Completed in {len(moves)} moves!")
        
    except ValueError:
        print("Please enter a valid number!")    #exception Handling

def display_initial(towers):
    max_height = max(len(v) for v in towers.values())
    for level in range(max_height, 0, -1):
        for tower_name in ['A', 'B', 'C']:
            if len(towers[tower_name]) >= level:
                disk = towers[tower_name][level - 1]
                print(f"  {disk:^6}", end=" ")
            else:
                print(f"  {'|':^6}", end=" ")
        print()
    print("  " + "-" * 20)
    print("   A      B      C\n")

if __name__ == "__main__":
    main()
