#!/usr/bin/env julia
using PyCall

unshift!(PyVector(pyimport("sys")["path"]), "")
@pyimport CopyPasta

server = listen(3001)
while true
    print("Listening...")
    conn = accept(server)
    @async begin
        try
            while true
                line = readline(conn)
                println(line)
                write(conn, join([CopyPasta.generate_copy_pasta(line), "\n"]))
                println("Written.")
            end
        catch err
            print("connection ended with error $err")
        end
    end
end

## using HttpServer
## using WebSockets

## wsh = WebSocketHandler() do req,client
##     while true
##         msg = read(client)
##         write(client, msg)
##     end
##   end

## server = Server(wsh)
## run(server, 3001)

## main()
