class Hero:
    def __init__(self, response):
        self.life = response['life']
        self.elo = response.get('elo', 0) # Bots have no elo
        self.gold = response['gold']
        self.userId = response.get('userId', 'bot') # Bot have no userId
        self.position = tuple(response['pos'].values())
        self.spawn = tuple(response['spawnPos'].values())
        self.crashed = response['crashed']
        self.mines = []
        self.id = response['id']
        self.name = response['name']

    def display(self, indent=0):
        disp_indent = lambda n: '    '*n
        print '[Player]'
        print disp_indent(indent) + '    life = %s' % self.life
        print disp_indent(indent) + '    elo = %s' % self.elo
        print disp_indent(indent) + '    gold = %s' % self.gold
        print disp_indent(indent) + '    userId = %s' % self.userId
        print disp_indent(indent) + '    position = %s' % str(self.position)
        print disp_indent(indent) + '    spawn = %s' % str(self.spawn)
        print disp_indent(indent) + '    crashed = %s' % self.crashed
        print disp_indent(indent) + '    mines = %s' % self.mines
        print disp_indent(indent) + '    id = %s' % self.id
        print disp_indent(indent) + '    name = %s' % self.name

