from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

print("=== Multiplayer Billiard Simulation Started ===")

# Connect ke CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

# Start simulation
sim.setStepping(False)
sim.startSimulation()

# Bola putih (cue ball)
cue_handle = sim.getObject("/Sphere[6]")

# Bola warna (misalnya Sphere[0] sampai Sphere[5])
ball_handles = [sim.getObject(f"/Sphere[{i}]") for i in range(6)]

# Tampilkan posisi awal
cue_pos = sim.getObjectPosition(cue_handle, -1)
print(f"Initial Cue Ball (Sphere[6]) Pos : {cue_pos}")

# Jumlah pemain
num_players = int(input("\nEnter number of players: "))

turn = 1
while True:
    print(f"\n=== Player {turn}'s Turn ===")

    # Input gaya & torsi dari player
    Fx = float(input("Enter Force X: "))
    Fy = float(input("Enter Force Y: "))
    Fz = float(input("Enter Force Z: "))
    Tx = float(input("Enter Torque X: "))
    Ty = float(input("Enter Torque Y: "))
    Tz = float(input("Enter Torque Z: "))

    # Terapkan ke bola putih
    sim.addForceAndTorque(cue_handle, [Fx, Fy, Fz], [Tx, Ty, Tz])
    sim.addStatusbarMessage(f"Player {turn} applied Force {Fx,Fy,Fz} and Torque {Tx,Ty,Tz}")

    # Tunggu agar bola bergerak
    time.sleep(5)

    # Tampilkan posisi bola putih
    cue_new = sim.getObjectPosition(cue_handle, -1)
    print(f"Cue Ball Pos : {cue_new}")

    # Tampilkan posisi semua bola warna
    for i, handle in enumerate(ball_handles):
        pos = sim.getObjectPosition(handle, -1)
        print(f"Ball {i} (Sphere[{i}]) Pos : {pos}")

    # Ganti ke player berikutnya
    turn += 1
    if turn > num_players:
        turn = 1  # balik ke Player 1

    # Tanya apakah lanjut
    cont = input("Continue to next turn? (y/n): ").lower()
    if cont != "y":
        break

# Stop simulation
sim.stopSimulation()
print("=== Simulation Finished ===")