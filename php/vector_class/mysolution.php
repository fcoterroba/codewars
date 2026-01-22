<?php
class Vector
{
    private array $components;

    function __construct(array $components)
    {
        $this->components = array_values($components);
    }

    public function add(Vector $other): Vector
    {
        $this->validateDimensions($other);
        $result = [];
        foreach ($this->components as $i => $val) {
            $result[] = $val + $other->components[$i];
        }
        return new Vector($result);
    }

    public function subtract(Vector $other): Vector
    {
        $this->validateDimensions($other);
        $result = [];
        foreach ($this->components as $i => $val) {
            $result[] = $val - $other->components[$i];
        }
        return new Vector($result);
    }

    public function dot(Vector $other)
    {
        $this->validateDimensions($other);
        $result = 0;
        foreach ($this->components as $i => $val) {
            $result += $val * $other->components[$i];
        }
        return $result;
    }

    public function norm(): float
    {
        $sumOfSquares = 0;
        foreach ($this->components as $val) {
            $sumOfSquares += $val * $val;
        }
        return sqrt($sumOfSquares);
    }

    public function equals(Vector $other): bool
    {
        if (count($this->components) !== count($other->components)) {
            return false;
        }
        foreach ($this->components as $i => $val) {
            if ($val != $other->components[$i]) {
                return false;
            }
        }
        return true;
    }

    public function __toString(): string
    {
        return '(' . implode(',', $this->components) . ')';
    }

    private function validateDimensions(Vector $other): void
    {
        if (count($this->components) !== count($other->components)) {
            throw new Exception();
        }
    }
}

// original kata: https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4
// my solution: https://www.codewars.com/kata/reviews/69286d6dc17ab8b5bb476f34/groups/6971d7b873949815a7ce1a1b