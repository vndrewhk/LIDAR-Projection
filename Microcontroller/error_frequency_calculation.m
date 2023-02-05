%% error frequency

clear all;
clc;

% change nmber here based on the delay number used in the arduino IDE
%~~~~~~~~~~~
delay = 0.05;                % (ms)
%~~~~~~~~~~~

f = 1000/delay;             % frequency depending on delay
n = zeros(1,floor(f));      % initializing matrix n that has a length of floor(f)
for i = 1:floor(f)          % n = [1 2 3 ... floor(f)]
    n(i) = i;
end
f_error = f./n             % error frequencies where siginificant amplitude information is lost (descendingn impact)

%% finding delay

clear all;
clc;
format shortG;

%~~~~~~~~~~~~~~~~~~~~~~~~~~~
f_target = 84 ;              % target signal frequency
%~~~~~~~~~~~~~~~~~~~~~~~~~~~

f_min = 2 * f_target;       % minimum sampling frequency to not lose frequency information according to sampling theorem
T_max = 1/f_min * 1000;     % maximum sampling delay time based on minimum sampling frequency
interval = 0.05;             % precision of delay time (ie. a precision of 0.5Hz means delay times of increments of 0.5ms used)
delay = [interval:interval:T_max];  % all the possible delay times 
f = 1000./delay;            % frequencies corresponding to the delay times

n = zeros(length(f), max(floor(f)));                    % integer matrix 
f_error = zeros(length(f), max(floor(f)));              % frequencies to avoid as amplitude information is significantly lost
f_ideal = zeros(length(f), max(floor(f))-1);            % frequencies right in the middle of adjacent error frequencies (error frequency being the frequencies to avoid)
deviation_local = zeros(length(f), max(floor(f))-1);    % calculating relative error about the ideal frequencies within each interval
result = zeros(length(f),4);                            % a matrix presenting the relative error and fraction order corresponding to each delay/frequency  

for i = 1:length(f)

    for j = 1:max(floor(f))             % integer matrix and error frequency calculations 
        if (j <= floor(f(i)))           
            n(i,j) = j;     
        else 
            n(i,j) = 0;
        end 
        f_error(i,j) = f(i)./n(i,j);
    end
  
    for k = 1:max(floor(f)-1)           % relative error calculations (be mindful to combine this for loop with the previous one, it is doable but would be less concise)
        if (k == 1)
            f_ideal(i,k) = Inf;
        elseif (j >= 2)
            f_ideal(i,k) = (f_error(i,k) + f_error(i,k+1))/2;    
        end
        deviation_local(i,k) = 100*abs((f_target - f_ideal(i,k))/(f_error(i,k+1) - f_error(i,k)));
    end

    [A,B] = min(deviation_local(i,:));  % finding minimum relative error for each delay/frequency
    result(i,1) = delay(i);             % delay time (theoretically the less the better, but requires more computing power as delay drcreases)
    result(i,2) = f(i);                 % frequencies corresponding to the delay times (theretically the greater the better)
    result(i,3) = [A];                  % relative error (theoretically the smaller the better, because this indicates how far away the signal frequency is from the ideal frequency)
    result(i,4) = [B];                  % fraction order (theoretically the greater the better, because a higher order has a smaller loss on the amplitude information)
end

disp("          d         f             e           o");    % d: delay time (ms), f: frequency (Hz), e:relative error (%), o:fraction order
disp(result);

% This code helps determine the relative error and fraction order
% corresponding to different delay times used, when a specific target
% signal frequency is expected to be detected. However, since
% computational power is a limitation and that compromises have to be made
% between relative errors and fraction orders, there is not an obvious
% answer. The best sampling frequency can be determined by expanding the
% code. (for instance, including codes to fully determine the impacts in 
% relation with relative error & fraction order, or give weighted decisions)
% (the fraction order seems to have the most impact and ideally o > 5~10)

%%

clear all;
clc;

global data graph_width;
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 graph_width = 500;                      % the number of data points to be presented in the graph
 data = zeros(1,graph_width);            % for sliding window control
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

%delete(instrfind);
%serial_object = serial('COM3','BaudRate',38400,'DataBits',16);
%serial_object = serial('COM3','BaudRate',38400,'ReadAsyncMode','continuous');
serial_object = serialport('COM3', 38400);                      % serial initialization (updated version of the old function serial() )
configureCallback(serial_object,"terminator",@callbackSerial)   % configuring callback whenever data available
fopen(serial_object);                                           % open serial port
% fclose(serial_object);
% clear serial_object

function callbackSerial(obj,~)          % callback function
    global data graph_width;
    v = fscanf(obj);                    % scan data being passed through the serial port
    value = str2double(v);              % data type conversion
    %disp(value);                   
    data(graph_width + 1) = value;      % sliding window control
    data(1) = [];                       % sliding window control
    %disp(data);    
    plot(data);                         % graph
    %drawnow();                          % force plot
end
