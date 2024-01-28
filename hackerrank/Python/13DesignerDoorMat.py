if __name__ == '__main__':
    height, width = input().split(' ')
    height =int(height)
    width = int(width)
    
    pipes = '.|.'
    mid = (height // 2)
    result = ''
    for i in range(height):
        if i < mid:
            n_pipes = (pipes * i) + pipes + (pipes * i)
            result += n_pipes.center(width, '-')
            result +='\n'
        elif i == mid:
            result += 'WELCOME'.center(width, '-')
            result +='\n'
        else:
            n_pipes = (pipes * (height-i-1)) + pipes + (pipes * (height-i-1))
            result += n_pipes.center(width, '-')
            result +='\n'
            
    print(result)