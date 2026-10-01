from collections import deque
import time

cola = deque()

cola.append("Ana")
cola.append("Carlos")
cola.append("Elena")

print("Cola actual:", list(cola))

time.sleep(2)
atendido = cola.popleft()

print("Se atendió a: ", atendido)
time.sleep(2)

print("Siguiente en la fila:", cola[0])
time.sleep(3)

print("Cola restante:", list(cola))
