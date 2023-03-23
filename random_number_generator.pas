PROGRAM random_number_generator;

type    
    r_nums = array of integer;

Var i,int,j,n,x,from,till,range : integer;
    numbers: r_nums;

procedure GenerateRandomNumbers(
    var till, range: integer
); 
begin
    SetLength(numbers, till);
    Randomize; 
    for i := 0 to till do
        begin
        int := Random(range + 1); 
        numbers[i] := int
    end;
end;

procedure BubbleSort( var a: array of integer );
begin
  n := high( a );
  for j := 0 to n - 1 do
    for i := 1 to n - 1 do
      if a[i] > a[i+1] then 
      begin
        x := a[i]; a[i] := a[i+1]; a[i+1] := x;
        end;
end;

procedure WriteNumbersFromArray( var a: array of integer );
begin 
    n := high(a);
    for i := 1 to n do
        write(a[i], ' ');
        end; 

begin
    till := 50;
    range := 100;
    GenerateRandomNumbers( till, range );
    WriteLn('Unsorted:');
    WriteNumbersFromArray(numbers);
    WriteLn('');
    BubbleSort(numbers);
    WriteLn('Bubble-sorted:');
    WriteNumbersFromArray(numbers);
end.
