## Logging Module in Python

- The logging module in Python makes it possible for an end user to create custom `logs` which are saved as files in order to understand important events that are happening within your code.

### Levels

- `Levels` essentially give an end user a higher abstract understanding of what's going on within the code. For example, let's say there is an action going on in the code which is not recommended, but doesn't necessarily break the code. This action would be referred to as a `warning`. The `warning` level is a popular one in the `logging` module in order to tell the end user some recommendations about how to fix problems for perfect code.

- More common levels that show up in logs are the `error` level and also the `info` level. The `info` level is used to give a user an indication that an event has just occurred in the code (doesn't really entail whether there's a problem). The `error` level takes place when the code actually breaks at a certain event. The location of the event with a message at the `error` level tells the end user where to look in order to solve the problem.

#### Specific Levels

- **INFO** : gives a user an indication that an event has just occurred

- **WARNING** : gives a recommendation to an end user that the action is not the optimal one, but doesn't break the code.

- **ERROR** : gives a user an indication that something is wrong with the code. Code breaks and pinpoints where to look to solve the problem.

### Usage

- The `logging` module is built-in to Python so it can be used by simply importing the package.

```python
import logging
```

Let's say you want to create a warning message in your log, you can do so with the following method:

```python
import logging

# Create a warning message
logging.warning('Be careful!')
```

- Custom configuration for your log

```python
import logging

# Create a custom format
fmt = '%(asctime)s %(user)-8s %(message)s'

logging.basicConfig(format=fmt)

# Create a dictionary to fill values
d = {'user' : 'rchatterjee'}

# Retrieve the logger
logger = logging.getLogger('sampleLogger')

# Warning message
logger.warning('There is an unexpected dependency resolution issue: %s', 'pandas', extra=d)
```
