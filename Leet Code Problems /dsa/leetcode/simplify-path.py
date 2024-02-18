class Solution:
    def simplifyPath(self, path: str) -> str:
        # Create an empty stack to keep track of directories
        stack = []
        
        # Split the input path into components using '/'
        components = path.split('/')
        
        # Iterate through the components of the path
        for component in components:
            # If the component is '..', move up one level in the directory structure
            if component == '..':
                # If the stack is not empty, pop the top element
                if stack:
                    stack.pop()
            # If the component is not empty or '.', it's a valid directory name
            elif component and component != '.':
                # Push the valid directory onto the stack
                stack.append(component)
        
        # Construct the simplified canonical path by joining the directories with '/'
       
        canonical_path = '/' + '/'.join(stack)
        
        
        # Return the simplified canonical path
        return canonical_path
        