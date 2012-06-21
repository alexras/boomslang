class StepType(object):
    validStepTypes = ["pre", "mid", "post", None]

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value not in StepType.validStepTypes:
            raise ValueError(
                "%s is not a valid step type. Valid step types are %s" \
                    % (value, ", ".join(map(str, StepType.validStepTypes))))

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if self.name not in instance.__dict__:
            raise AttributeError, self.name

        return instance.__dict__[self.name]
