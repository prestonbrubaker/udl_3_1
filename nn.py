import random
import pygame
import time
import math

pygame.init()

window = pygame.display.set_mode((700, 700))

font = pygame.font.Font(None, 17)

weights = []

itC = 0

loss = 0


for n in range(0, 10):
    weights.append(random.uniform(-1,1))


weights_try = []

for n in range(0, 10):
    weights_try.append(weights[n])



def activation(x_inn):

    if(x_inn < 0):
        output = 0
    elif(x_inn >= 0):
        output = x_inn
    
    return output


def nn_forward(x_in, weights_in):
    nodes = []
    for n in range(0, 7):
        nodes.append(0)
    
    # Initialize input layer and biases

    nodes[0] = 1

    nodes[1] = x_in

    nodes [2] = 1

    nodes[6] = weights_in[6] + weights_in[7] * activation(weights_in[0] + weights_in[3] * nodes[1]) + weights_in[8] * activation(weights_in[1] + weights_in[4] * nodes[1]) + weights_in[9] * activation(weights_in[2] + weights_in[5] * nodes[1])
    
    # Return output
    return nodes[6]




def display():
    window.fill((100, 100, 100))
    for k in range(0, 400):
        x = k / 400
        y = nn_forward(x, weights)
        y_desired = math.sin(x * math.pi)
        if(x < 0.5):
            y_desired = 0
        else:
            y_desired = 1
        
        x_disp = x * 700
        y_disp = 700 * 4 / 5 - y * 700 / 2
        y_desired_disp = 700 * 4 / 5 - y_desired * 700 / 2

        
        pygame.draw.rect(window, (0, 255, 0), (x_disp, y_desired_disp, 2, 2))
        pygame.draw.rect(window, (255, 0, 0), (x_disp, y_disp, 2, 2))

    # Draw brain

    off_x = 250
    off_y = 50

    node_0 = (0 + off_x, 33 + off_y)
    node_1 = (0 + off_x, 66 + off_y)

    node_2 = (100 + off_x, 0 + off_y)
    node_3 = (100 + off_x, 33 + off_y)
    node_4 = (100 + off_x, 66 + off_y)
    node_5 = (100 + off_x, 100 + off_y)

    node_6 = (200 + off_x, 50 + off_y) 

    max_val = max(weights)
    min_val = min(weights)
    



    # pygame.draw.line(surface, color, start_pos, end_pos, width)

    pygame.draw.line(window, ((weights[0] - min_val) / (max_val - min_val) * 255, 0, 0), node_0, node_3, 2)
    pygame.draw.line(window, ((weights[1] - min_val) / (max_val - min_val) * 255, 0, 0), node_0, node_4, 2)
    pygame.draw.line(window, ((weights[2] - min_val) / (max_val - min_val) * 255, 0, 0), node_0, node_5, 2)
    pygame.draw.line(window, ((weights[3] - min_val) / (max_val - min_val) * 255, 0, 0), node_1, node_3, 2)
    pygame.draw.line(window, ((weights[4] - min_val) / (max_val - min_val) * 255, 0, 0), node_1, node_4, 2)
    pygame.draw.line(window, ((weights[5] - min_val) / (max_val - min_val) * 255, 0, 0), node_1, node_5, 2)
        
    pygame.draw.line(window, ((weights[6] - min_val) / (max_val - min_val) * 255, 0, 0), node_2, node_6, 2)
    pygame.draw.line(window, ((weights[7] - min_val) / (max_val - min_val) * 255, 0, 0), node_3, node_6, 2)
    pygame.draw.line(window, ((weights[8] - min_val) / (max_val - min_val) * 255, 0, 0), node_4, node_6, 2)
    pygame.draw.line(window, ((weights[9] - min_val) / (max_val - min_val) * 255, 0, 0), node_5, node_6, 2)


    # pygame.draw.circle(surface, color, center, radius, width)
    pygame.draw.circle(window, (255, 0, 0), node_0, 7, 0)
    pygame.draw.circle(window, (255, 0, 0), node_1, 7, 0)

    pygame.draw.circle(window, (255, 0, 0), node_2, 7, 0)
    pygame.draw.circle(window, (255, 0, 0), node_3, 7, 0)
    pygame.draw.circle(window, (255, 0, 0), node_4, 7, 0)
    pygame.draw.circle(window, (255, 0, 0), node_5, 7, 0)

    pygame.draw.circle(window, (255, 0, 0), node_6, 7, 0)

    window.blit(font.render("x input", True, (255, 255, 255)), (200, 110))
    window.blit(font.render("bias node", True, (255, 255, 255)), (185, 77))
    window.blit(font.render("bias node", True, (255, 255, 255)), (285, 45))
    window.blit(font.render("guess for y", True, (255, 255, 255)), (462, 93))

    window.blit(font.render("Weights:", True, (255, 255, 255)), (180, 600))

    

    for n in range(0, 3):
        for i in range(0, 3):
            window.blit(font.render(str(round(weights[n + 3 * i], 3)), True, (255, 255, 255)), (250 + n * 50, 600 + i * 20))
    window.blit(font.render(str(round(weights[9], 3)), True, (255, 255, 255)), (250, 600 + 3 * 20))

    
    window.blit(font.render("Iteration: " + str(itC), True, (255, 255, 255)), (500, 600))
    window.blit(font.render("Loss: " + str(round(loss, 3)), True, (255, 255, 255)), (500, 620))

    pygame.display.flip()


def gen_loss(weights_in):
    loss = 0
    for k in range(0, 200):
        x = k / 200
        y = nn_forward(x, weights_in)
        y_desired = math.sin(x * math.pi)
        if(x < 0.5):
            y_desired = 0
        else:
            y_desired = 1
        loss += ( y_desired - y ) ** 2
    
    return loss



while True:

    display()

    if(itC == 0):
        time.sleep(1)

    #time.sleep(1)

    loss = gen_loss(weights)

    print("Iteration: " + str(itC) + " Loss: " + str(loss))
    #print(weights)

    weights_try = []
    for n in range(0, 10):
        weights_try.append( weights[n] )

    n = random.randint(0, 9)

    mut = 1 * random.uniform(-1, 1)
    mag = 10 ** random.randint(-11, 1)

    weights_try[n] += mut * mag

    if(weights_try[n] > 20):
        weights_try[n] = 20
    if(weights_try[n] < -20):
        weights_try[n] = -20

    loss_try = gen_loss(weights_try)

    if ( loss_try - random.uniform(0, loss * .001)<= loss):
        weights = []
        for n in range(0, 10):
            weights.append( weights_try[n] )


    
    itC += 1

