`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    23:21:26 01/20/2019 
// Design Name: 
// Module Name:    Controller 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module Controller(
input clk,
input first_police_interrupt,
input second_police_interrupt,
input first_pedestrian_interrupt,
input second_pedestrian_interrupt,
output reg [2:0]first_carsLights,
output reg [2:0]second_carsLights,
output reg [1:0]first_pedestrianLights,
output reg [1:0]second_pedestrianLights
    );
	 reg [6:0]reg_time = -1;
	 reg [5:0]first_interrupt = 0;
	 reg [5:0]second_interrupt= 0;
	 initial begin
	 first_carsLights = 3'b001;
	 second_carsLights = 3'b100;
	 second_pedestrianLights = 2'b01;
	 first_pedestrianLights = 2'b10;
	 end
	 always @(clk, second_police_interrupt, first_police_interrupt, first_pedestrian_interrupt, second_pedestrian_interrupt)
	 begin
		
		if (!clk | clk)
		begin
			reg_time = reg_time + 1;
		end
		
		if (first_police_interrupt)
		begin
			if (first_carsLights == 3'b001)
			begin
				reg_time = 9;
			end
			else if(second_carsLights == 3'b100)
			begin
				reg_time = 21;
			end
		end
		if (second_police_interrupt)
		begin
			if (first_carsLights == 3'b001)
			begin
				reg_time = 9;
			end
			else if(second_carsLights == 3'b100)
			begin
				reg_time = 21;
			end
		end
		
		if (first_pedestrian_interrupt && reg_time > 22&& first_interrupt <2)
		begin
			if (first_pedestrianLights == 2'b01)
			begin
				first_interrupt = first_interrupt + 1;
				reg_time =21;
			end
		end
		if (second_pedestrian_interrupt && reg_time > 10 && second_interrupt <2)
		begin 
			if (second_pedestrianLights == 2'b01)
			begin
				second_interrupt = second_interrupt + 1;
				reg_time = 9;
			end
		
		end
		
		
		
		
		
		if (reg_time == 9)
		begin
			first_carsLights = 3'b010;
		end
		if (reg_time == 13)
		begin
			first_carsLights = 3'b100;
			second_carsLights = 3'b001;
			first_pedestrianLights = 2'b01;
			second_pedestrianLights = 2'b10;
			second_interrupt = 0;
		end 
		if ( reg_time == 21 )
		begin 
			second_carsLights = 3'b010;
		end
		if ( reg_time == 25)
		begin 
			first_carsLights = 3'b001;
			second_carsLights = 3'b100;
			first_pedestrianLights = 2'b10;
			second_pedestrianLights = 2'b01;
			first_interrupt = 0;
			reg_time = -1;
		end
		
		
	 end
	 
	always @(clk)
	begin
		// where we're going to write on a file with open it on a append mode
		// with every run of this verilog code the output of its module will be write to a file name text.txt
		$fwrite($fopen ("test.txt", "a"), "clk:%b,first_carsLights:%b,second_carsLights:%b,first_pedestrianLights:%b,second_pedestrianLights:%b,reg_time:%d-", clk, first_carsLights, second_carsLights, first_pedestrianLights,second_pedestrianLights, reg_time);
	end

endmodule
