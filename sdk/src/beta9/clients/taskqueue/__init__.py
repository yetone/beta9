# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: taskqueue.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Dict,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class TaskQueuePutRequest(betterproto.Message):
    stub_id: str = betterproto.string_field(1)
    payload: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class TaskQueuePutResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    task_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class TaskQueuePopRequest(betterproto.Message):
    stub_id: str = betterproto.string_field(1)
    container_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class TaskQueuePopResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    task_msg: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class TaskQueueLengthRequest(betterproto.Message):
    stub_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class TaskQueueLengthResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    length: int = betterproto.int64_field(2)


@dataclass(eq=False, repr=False)
class TaskQueueCompleteRequest(betterproto.Message):
    task_id: str = betterproto.string_field(1)
    stub_id: str = betterproto.string_field(2)
    task_duration: float = betterproto.float_field(3)
    task_status: str = betterproto.string_field(4)
    container_id: str = betterproto.string_field(5)
    container_hostname: str = betterproto.string_field(6)
    keep_warm_seconds: float = betterproto.float_field(7)


@dataclass(eq=False, repr=False)
class TaskQueueCompleteResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class TaskQueueMonitorRequest(betterproto.Message):
    task_id: str = betterproto.string_field(1)
    stub_id: str = betterproto.string_field(2)
    container_id: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class TaskQueueMonitorResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    cancelled: bool = betterproto.bool_field(2)
    complete: bool = betterproto.bool_field(3)
    timed_out: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class StartTaskQueueServeRequest(betterproto.Message):
    stub_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class StartTaskQueueServeResponse(betterproto.Message):
    output: str = betterproto.string_field(1)
    done: bool = betterproto.bool_field(2)
    exit_code: int = betterproto.int32_field(3)


@dataclass(eq=False, repr=False)
class StopTaskQueueServeRequest(betterproto.Message):
    stub_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class StopTaskQueueServeResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)


class TaskQueueServiceStub(betterproto.ServiceStub):
    async def task_queue_put(
        self,
        task_queue_put_request: "TaskQueuePutRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "TaskQueuePutResponse":
        return await self._unary_unary(
            "/taskqueue.TaskQueueService/TaskQueuePut",
            task_queue_put_request,
            TaskQueuePutResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def task_queue_pop(
        self,
        task_queue_pop_request: "TaskQueuePopRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "TaskQueuePopResponse":
        return await self._unary_unary(
            "/taskqueue.TaskQueueService/TaskQueuePop",
            task_queue_pop_request,
            TaskQueuePopResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def task_queue_monitor(
        self,
        task_queue_monitor_request: "TaskQueueMonitorRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["TaskQueueMonitorResponse"]:
        async for response in self._unary_stream(
            "/taskqueue.TaskQueueService/TaskQueueMonitor",
            task_queue_monitor_request,
            TaskQueueMonitorResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def task_queue_complete(
        self,
        task_queue_complete_request: "TaskQueueCompleteRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "TaskQueueCompleteResponse":
        return await self._unary_unary(
            "/taskqueue.TaskQueueService/TaskQueueComplete",
            task_queue_complete_request,
            TaskQueueCompleteResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def task_queue_length(
        self,
        task_queue_length_request: "TaskQueueLengthRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "TaskQueueLengthResponse":
        return await self._unary_unary(
            "/taskqueue.TaskQueueService/TaskQueueLength",
            task_queue_length_request,
            TaskQueueLengthResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def start_task_queue_serve(
        self,
        start_task_queue_serve_request: "StartTaskQueueServeRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["StartTaskQueueServeResponse"]:
        async for response in self._unary_stream(
            "/taskqueue.TaskQueueService/StartTaskQueueServe",
            start_task_queue_serve_request,
            StartTaskQueueServeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def stop_task_queue_serve(
        self,
        stop_task_queue_serve_request: "StopTaskQueueServeRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "StopTaskQueueServeResponse":
        return await self._unary_unary(
            "/taskqueue.TaskQueueService/StopTaskQueueServe",
            stop_task_queue_serve_request,
            StopTaskQueueServeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class TaskQueueServiceBase(ServiceBase):
    async def task_queue_put(
        self, task_queue_put_request: "TaskQueuePutRequest"
    ) -> "TaskQueuePutResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def task_queue_pop(
        self, task_queue_pop_request: "TaskQueuePopRequest"
    ) -> "TaskQueuePopResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def task_queue_monitor(
        self, task_queue_monitor_request: "TaskQueueMonitorRequest"
    ) -> AsyncIterator["TaskQueueMonitorResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
        yield TaskQueueMonitorResponse()

    async def task_queue_complete(
        self, task_queue_complete_request: "TaskQueueCompleteRequest"
    ) -> "TaskQueueCompleteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def task_queue_length(
        self, task_queue_length_request: "TaskQueueLengthRequest"
    ) -> "TaskQueueLengthResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def start_task_queue_serve(
        self, start_task_queue_serve_request: "StartTaskQueueServeRequest"
    ) -> AsyncIterator["StartTaskQueueServeResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
        yield StartTaskQueueServeResponse()

    async def stop_task_queue_serve(
        self, stop_task_queue_serve_request: "StopTaskQueueServeRequest"
    ) -> "StopTaskQueueServeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_task_queue_put(
        self, stream: "grpclib.server.Stream[TaskQueuePutRequest, TaskQueuePutResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.task_queue_put(request)
        await stream.send_message(response)

    async def __rpc_task_queue_pop(
        self, stream: "grpclib.server.Stream[TaskQueuePopRequest, TaskQueuePopResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.task_queue_pop(request)
        await stream.send_message(response)

    async def __rpc_task_queue_monitor(
        self,
        stream: "grpclib.server.Stream[TaskQueueMonitorRequest, TaskQueueMonitorResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.task_queue_monitor,
            stream,
            request,
        )

    async def __rpc_task_queue_complete(
        self,
        stream: "grpclib.server.Stream[TaskQueueCompleteRequest, TaskQueueCompleteResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.task_queue_complete(request)
        await stream.send_message(response)

    async def __rpc_task_queue_length(
        self,
        stream: "grpclib.server.Stream[TaskQueueLengthRequest, TaskQueueLengthResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.task_queue_length(request)
        await stream.send_message(response)

    async def __rpc_start_task_queue_serve(
        self,
        stream: "grpclib.server.Stream[StartTaskQueueServeRequest, StartTaskQueueServeResponse]",
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.start_task_queue_serve,
            stream,
            request,
        )

    async def __rpc_stop_task_queue_serve(
        self,
        stream: "grpclib.server.Stream[StopTaskQueueServeRequest, StopTaskQueueServeResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.stop_task_queue_serve(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/taskqueue.TaskQueueService/TaskQueuePut": grpclib.const.Handler(
                self.__rpc_task_queue_put,
                grpclib.const.Cardinality.UNARY_UNARY,
                TaskQueuePutRequest,
                TaskQueuePutResponse,
            ),
            "/taskqueue.TaskQueueService/TaskQueuePop": grpclib.const.Handler(
                self.__rpc_task_queue_pop,
                grpclib.const.Cardinality.UNARY_UNARY,
                TaskQueuePopRequest,
                TaskQueuePopResponse,
            ),
            "/taskqueue.TaskQueueService/TaskQueueMonitor": grpclib.const.Handler(
                self.__rpc_task_queue_monitor,
                grpclib.const.Cardinality.UNARY_STREAM,
                TaskQueueMonitorRequest,
                TaskQueueMonitorResponse,
            ),
            "/taskqueue.TaskQueueService/TaskQueueComplete": grpclib.const.Handler(
                self.__rpc_task_queue_complete,
                grpclib.const.Cardinality.UNARY_UNARY,
                TaskQueueCompleteRequest,
                TaskQueueCompleteResponse,
            ),
            "/taskqueue.TaskQueueService/TaskQueueLength": grpclib.const.Handler(
                self.__rpc_task_queue_length,
                grpclib.const.Cardinality.UNARY_UNARY,
                TaskQueueLengthRequest,
                TaskQueueLengthResponse,
            ),
            "/taskqueue.TaskQueueService/StartTaskQueueServe": grpclib.const.Handler(
                self.__rpc_start_task_queue_serve,
                grpclib.const.Cardinality.UNARY_STREAM,
                StartTaskQueueServeRequest,
                StartTaskQueueServeResponse,
            ),
            "/taskqueue.TaskQueueService/StopTaskQueueServe": grpclib.const.Handler(
                self.__rpc_stop_task_queue_serve,
                grpclib.const.Cardinality.UNARY_UNARY,
                StopTaskQueueServeRequest,
                StopTaskQueueServeResponse,
            ),
        }
