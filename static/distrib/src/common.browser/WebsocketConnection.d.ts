import { ConnectionEvent, ConnectionMessage, ConnectionOpenResponse, ConnectionState, EventSource, IConnection, IStringDictionary, IWebsocketMessageFormatter, Promise } from "../common/Exports";
import { RecognitionAPI } from "../sdk/speech/Exports";
export declare class WebsocketConnection implements IConnection {
    private uri;
    private messageFormatter;
    private connectionMessageAdapter;
    private id;
    private isDisposed;
    constructor(uri: string, queryParameters: IStringDictionary<string>, headers: IStringDictionary<string>, messageFormatter: IWebsocketMessageFormatter, recognitionAPI: RecognitionAPI, endpointId: string, connectionId?: string);
    Dispose: () => void;
    IsDisposed: () => boolean;
    readonly Id: string;
    State: () => ConnectionState;
    Open: () => Promise<ConnectionOpenResponse>;
    Send: (message: ConnectionMessage) => Promise<boolean>;
    Read: () => Promise<ConnectionMessage>;
    readonly Events: EventSource<ConnectionEvent>;
}
