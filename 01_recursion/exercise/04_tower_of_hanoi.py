class Rod:
    def __init__(self, ll: list, name: str) -> None:
        self.ll = ll
        self.name = name

    def print_rod(self):
        spaces = " "*(3-len(self.name))
        print(f'{self.name}{spaces}: {" ".join(map(str, self.ll))}')


def print_rods():
    print()
    source_rod.print_rod()
    spare_rod.print_rod()
    destination_rod.print_rod()
    print()


def print_step(count, el, name):
    print(f'Step #{count}: Element {el} => Rod {name}')


def move_elements(bottom_el, source, spare, destination):
    if bottom_el == 1:
        destination.ll.append(source.ll.pop())
        steps.append(1)
        print_step(len(steps), bottom_el, destination.name)
        print_rods()
    else:
        # move all els above bottom from source to spare
        move_elements(bottom_el=bottom_el-1, source=source,
                      spare=destination, destination=spare,)

        steps.append(1)
        print_step(len(steps), bottom_el, destination.name)

        destination.ll.append(source.ll.pop())

        print_rods()

        # move all els from spare to destination
        move_elements(bottom_el-1, source=spare,
                      spare=source, destination=destination)


n = int(input('Write the number of elements: '))

source_rod = Rod([el for el in range(n, 0, -1)], 'I')
spare_rod = Rod([], 'II')
destination_rod = Rod([], 'III')
steps = []

print_rods()
move_elements(n, source_rod, spare_rod, destination_rod)
print(f'Completed in {len(steps)} steps.')
