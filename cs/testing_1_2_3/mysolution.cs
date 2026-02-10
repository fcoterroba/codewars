using System.Collections.Generic;

public class LineNumbering 
{
    public static List<string> Number(List<string> lines) 
    {
        return lines.Select((line, index) => $"{index + 1}: {line}").ToList();
    }
}

// original kata: https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
// my solution: https://www.codewars.com/kata/reviews/5e4f3b4a77d51a0001efedd2/groups/62258b4bbb23e50001a3f29e